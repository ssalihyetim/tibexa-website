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
CSV_PATH = os.path.join(os.path.dirname(__file__), "TGpartnershipv3.csv")
OUTPUT_PATH = os.path.join(os.path.dirname(__file__), "icebreakers_output.csv")

LIMIT = None          # None = tüm liste
GEMINI_CONCURRENCY = 20   # paralel Gemini çağrısı
CRAWL_CONCURRENCY = 5     # paralel web crawl

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
        return None, f"Boş içerik ({url})"
    except Exception as e:
        return None, f"{url}: {e}"


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


async def generate_icebreaker(session, crawler, row, gemini_sem, crawl_sem, counter, total):
    name = row.get('Full Name', 'Unknown')
    company = row.get('Company Name', '') or row.get('Org', '')
    web_error = None
    website_text = None

    # Web crawl — ayrı semaphore
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
        try:
            async with session.post(API_URL, json=payload, timeout=aiohttp.ClientTimeout(total=30)) as resp:
                done = counter['done'] + 1
                counter['done'] = done
                pct = done / total * 100

                if resp.status != 200:
                    error_text = await resp.text()
                    counter['errors'] += 1
                    print(f"[{done}/{total} {pct:.1f}%] HATA Gemini [{name}]: HTTP {resp.status}")
                    icebreaker = f"HATA_GEMINI: HTTP {resp.status}"
                else:
                    data = await resp.json()
                    icebreaker = data["candidates"][0]["content"]["parts"][0]["text"].strip()
                    web_note = f" [WEB_HATA: {web_error}]" if web_error and not website_text else ""
                    web_note = " [WEB_CEKEMEDI]" if web_error and not website_text else ""
                    print(f"[{done}/{total} {pct:.1f}%] OK {name} @ {company}{web_note}")

        except Exception as e:
            counter['done'] = counter['done']  # zaten artırıldı
            counter['errors'] += 1
            print(f"[{counter['done']}/{total}] HATA [{name}]: {e}")
            icebreaker = f"HATA: {e}"

    web_fetch_status = ""
    if not has_useful_description(row):
        if website_text:
            web_fetch_status = "WEB_CEKTI"
        elif web_error:
            web_fetch_status = f"WEB_HATA: {web_error[:100]}"
        else:
            web_fetch_status = "WEB_URL_YOK"

    return {**row, "Icebreaker": icebreaker, "WebFetchStatus": web_fetch_status}


async def main():
    rows = []
    with open(CSV_PATH, "r", encoding="utf-8") as f:
        reader = csv.DictReader(f)
        for i, row in enumerate(reader):
            if LIMIT and i >= LIMIT:
                break
            rows.append(row)

    total = len(rows)
    print(f"\n{total} kişi için icebreaker üretiliyor...")
    print(f"Gemini paralel: {GEMINI_CONCURRENCY} | Web crawl paralel: {CRAWL_CONCURRENCY}\n")

    counter = {'done': 0, 'errors': 0}
    gemini_sem = asyncio.Semaphore(GEMINI_CONCURRENCY)
    crawl_sem = asyncio.Semaphore(CRAWL_CONCURRENCY)

    async with aiohttp.ClientSession() as session:
        async with AsyncWebCrawler(verbose=False) as crawler:
            tasks = [
                generate_icebreaker(session, crawler, row, gemini_sem, crawl_sem, counter, total)
                for row in rows
            ]
            results = await asyncio.gather(*tasks)

    # Çekilemeyenleri raporla
    web_errors = [r for r in results if r.get('WebFetchStatus', '').startswith('WEB_HATA')]
    no_url = [r for r in results if r.get('WebFetchStatus') == 'WEB_URL_YOK']
    gemini_errors = [r for r in results if r.get('Icebreaker', '').startswith('HATA')]

    # CSV'ye yaz
    fieldnames = list(results[0].keys())
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(results)

    print(f"\n{'='*50}")
    print(f"TAMAMLANDI: {total} kişi işlendi")
    print(f"Gemini hatası: {len(gemini_errors)}")
    print(f"Web çekilemedi: {len(web_errors)}")
    print(f"Web URL yok: {len(no_url)}")
    if web_errors:
        print(f"\nWeb çekilemeyen firmalar ({len(web_errors)}):")
        for r in web_errors[:20]:
            print(f"  - {r.get('Company Name','')} | {r.get('Company Website','')} | {r.get('WebFetchStatus','')}")
        if len(web_errors) > 20:
            print(f"  ... ve {len(web_errors)-20} tane daha")
    print(f"\nÇıktı: {OUTPUT_PATH}")


if __name__ == "__main__":
    asyncio.run(main())
