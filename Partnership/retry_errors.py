import csv
import os
import asyncio
import aiohttp
from dotenv import load_dotenv
from crawl4ai import AsyncWebCrawler

load_dotenv(os.path.join(os.path.dirname(__file__), '..', '.env.local'))

API_KEY = os.getenv("GEMINI_API_KEY")
MODEL = "gemini-2.5-flash"
API_URL = f"https://generativelanguage.googleapis.com/v1beta/models/{MODEL}:generateContent?key={API_KEY}"
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "icebreakers_output.csv")

GEMINI_CONCURRENCY = 3   # düşük — rate limit önlemek için
CRAWL_CONCURRENCY = 3
RETRY_DELAY = 2.0        # 429 sonrası saniye bekle
MAX_RETRIES = 3

SYSTEM_PROMPT = """Sen bir B2B cold email uzmanısın.

Sana bir firma ve o firmadaki kişi hakkında bilgi vereceğim. Bu kişiye gönderilecek cold email'in açılış cümlesi olan 1 cümlelik bir icebreaker yazmanı istiyorum.

Icebreaker kuralları:
- Sadece 1 cümle yaz, başka bir şey yazma
- Firmaya özel somut bir gözlem veya övgü olsun (kuruluş yılı, sektördeki konumu, büyüme, spesifik bir hizmet, lokasyon avantajı gibi)
- İşlerine dair bir gözlemde bulun.
- Türkçe dilbilgisi kurallarına uy.
- Firma açıklaması İngilizce olsa bile Türkçe yaz
- "Gördüm", "dikkatimi çekti", "takip ediyorum" gibi doğal ifadeler kullanabilirsin
- Genel ve klişe cümlelerden kaçın — "sektörde öncü", "lider firma" gibi boş övgüler yazma
- Eğer firma açıklaması çok genel veya boşsa, sektör ve lokasyon bilgisinden yola çıkarak somut bir şey yaz"""

GENERIC_PATTERNS = [
    "is a management consulting company based out of",
    "is a company based",
    "is based out of",
]


def has_useful_description(row):
    desc = (row.get('Company Description') or '').strip()
    seo = (row.get('Company SEO Description') or '').strip()
    services = (row.get('Company Product and Services') or '').strip()
    if services:
        return True
    for pattern in GENERIC_PATTERNS:
        if pattern in desc:
            return False
    if len(desc) > 80:
        return True
    if len(seo) > 40:
        return True
    return False


async def fetch_website(crawler, url):
    if not url:
        return None, "URL yok"
    url = url.strip()
    if not url.startswith('http'):
        url = 'https://' + url
    try:
        result = await crawler.arun(url=url, timeout=15)
        if result.success and result.markdown:
            return result.markdown[:2000], None
        return None, f"Boş içerik"
    except Exception as e:
        return None, str(e)[:80]


def build_user_prompt(row, website_text=None):
    parts = []
    parts.append(f"Kişi: {row.get('Full Name', '')} — {row.get('Title', '')}")
    parts.append(f"Firma: {row.get('Company Name', '') or row.get('Org', '')}")
    if row.get('Company Industry'):
        parts.append(f"Sektör: {row['Company Industry']}")
    if row.get('Company Product and Services'):
        parts.append(f"Hizmetler: {row['Company Product and Services']}")
    if row.get('Company Description'):
        parts.append(f"Firma Açıklaması (LinkedIn): {row['Company Description'][:500]}")
    if row.get('Company SEO Description'):
        parts.append(f"SEO Açıklaması: {row['Company SEO Description'][:300]}")
    if website_text:
        parts.append(f"Web Sitesi İçeriği: {website_text}")
    if row.get('City'):
        parts.append(f"Şehir: {row['City']}")
    if row.get('Company Founding Year'):
        parts.append(f"Kuruluş Yılı: {row['Company Founding Year']}")
    if row.get('Company Employee Count'):
        parts.append(f"Çalışan Sayısı: {row['Company Employee Count']}")
    return "\n".join(parts)


async def call_gemini(session, payload, retries=MAX_RETRIES):
    for attempt in range(retries):
        async with session.post(API_URL, json=payload, timeout=aiohttp.ClientTimeout(total=30)) as resp:
            if resp.status == 429:
                wait = RETRY_DELAY * (2 ** attempt)
                print(f"    429 rate limit — {wait:.0f}s bekleniyor...")
                await asyncio.sleep(wait)
                continue
            if resp.status != 200:
                error_text = await resp.text()
                return None, f"HTTP {resp.status}: {error_text[:100]}"
            data = await resp.json()
            text = data["candidates"][0]["content"]["parts"][0]["text"].strip()
            return text, None
    return None, "MAX_RETRY aşıldı (429)"


async def process_row(session, crawler, row, gemini_sem, crawl_sem, counter, total):
    name = row.get('Full Name', 'Unknown')
    company = row.get('Company Name', '') or row.get('Org', '')
    web_error = None
    website_text = None

    if not has_useful_description(row):
        website_url = row.get('Company Website', '')
        async with crawl_sem:
            website_text, web_error = await fetch_website(crawler, website_url)

    user_prompt = build_user_prompt(row, website_text)
    payload = {
        "contents": [{"role": "user", "parts": [{"text": f"{SYSTEM_PROMPT}\n\n---\n\n{user_prompt}"}]}],
        "generationConfig": {
            "temperature": 0.7,
            "maxOutputTokens": 1024,
            "thinkingConfig": {"thinkingBudget": 0}
        }
    }

    async with gemini_sem:
        icebreaker, err = await call_gemini(session, payload)

    counter['done'] += 1
    done = counter['done']
    pct = done / total * 100

    if err:
        counter['errors'] += 1
        print(f"[{done}/{total} {pct:.1f}%] HATA {name} @ {company}: {err}")
        icebreaker = f"HATA: {err}"
    else:
        web_note = " [WEB_CEKEMEDI]" if web_error and not website_text else ""
        print(f"[{done}/{total} {pct:.1f}%] OK {name} @ {company}{web_note}")

    web_status = ""
    if not has_useful_description(row):
        web_status = "WEB_CEKTI" if website_text else f"WEB_HATA: {web_error or 'URL yok'}"

    return {**row, "Icebreaker": icebreaker, "WebFetchStatus": web_status}


async def main():
    # Mevcut output'u oku
    print("Mevcut output okunuyor...")
    existing = {}
    fieldnames = None
    try:
        with open(OUTPUT_PATH, "r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            fieldnames = reader.fieldnames
            for row in reader:
                key = row.get('Email Business') or row.get('Full Name', '')
                existing[key] = row
    except FileNotFoundError:
        print("Output dosyası bulunamadı — hepsini çalıştırın.")
        return

    # Sadece hatalı olanları filtrele
    to_retry = []
    ok_rows = []
    for key, row in existing.items():
        icebreaker = row.get('Icebreaker', '')
        if icebreaker.startswith('HATA'):
            to_retry.append(row)
        else:
            ok_rows.append(row)

    print(f"Toplam: {len(existing)} | Başarılı: {len(ok_rows)} | Retry edilecek: {len(to_retry)}\n")

    if not to_retry:
        print("Retry edilecek satır yok!")
        return

    counter = {'done': 0, 'errors': 0}
    gemini_sem = asyncio.Semaphore(GEMINI_CONCURRENCY)
    crawl_sem = asyncio.Semaphore(CRAWL_CONCURRENCY)
    total = len(to_retry)

    async with aiohttp.ClientSession() as session:
        async with AsyncWebCrawler(verbose=False) as crawler:
            tasks = [
                process_row(session, crawler, row, gemini_sem, crawl_sem, counter, total)
                for row in to_retry
            ]
            retried = await asyncio.gather(*tasks)

    # Merge: ok_rows + retried
    all_rows = ok_rows + list(retried)

    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(all_rows)

    still_errors = [r for r in retried if r.get('Icebreaker', '').startswith('HATA')]
    print(f"\n{'='*50}")
    print(f"TAMAMLANDI — {total} retry işlendi")
    print(f"Başarılı: {total - len(still_errors)} | Hâlâ hata: {len(still_errors)}")
    print(f"Çıktı güncellendi: {OUTPUT_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
