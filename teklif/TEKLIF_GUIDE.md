# Tibexa — Teklif Hazırlama Rehberi

Bu rehber, müşterilere sunulacak teklif dosyalarının yapısını, dilini ve teknik altyapısını tanımlar. Orzax teklifi referans alınarak oluşturulmuştur.

---

## 1. Dosya & Yayınlama

| Konu | Kural |
|---|---|
| Klasör | `/teklif/` altında, müşteri adıyla: `teklif/musteri.html` |
| Format | Tek dosya, self-contained HTML. Harici bağımlılık sadece Google Fonts. |
| Navigasyon | Sitede hiçbir yerde link verilmez. URL sadece müşteriye gönderilir. |
| SEO engeli | `<meta name="robots" content="noindex, nofollow">` + `robots.txt` → `Disallow: /teklif/` |
| Sitemap | Teklif dosyaları sitemap.xml'e eklenmez. |
| Logo | Müşteri logosunun beyaz/transparan versiyonu `teklif/` klasöründe tutulur. |

---

## 2. Tasarım Sistemi

### Renk Paleti (CSS Variables)

```css
--black: #0a0a0a;      /* Arka plan */
--dark: #111318;        /* Koyu kart */
--card: #181c24;        /* Kart arka planı */
--card2: #1e2330;       /* İkincil kart */
--border: rgba(255,255,255,0.07);
--white: #f4f4f0;       /* Ana metin */
--muted: #8a8f9e;       /* İkincil metin */
--accent: #c9a84c;      /* Altın vurgu */
--accent2: #e8c96a;     /* Açık altın */
--green: #3ecf8e;       /* Pozitif/başarı */
--red: #f55;            /* Negatif/uyarı */
--blue: #5b9cf6;        /* Yöntem A rengi */
```

### Tipografi
- **Font:** Red Hat Display (300–900)
- **H1:** clamp(42px, 6vw, 80px), weight 800
- **H2:** clamp(28px, 4vw, 48px), weight 700
- **H3:** 18px, weight 700
- **Body:** 15px, line-height 1.7, color `--muted`
- **Label:** 10px, letter-spacing 4px, uppercase, color `--accent`

### Slide Sistemi
- Her slide tam ekran (100vw × 100vh), yatay scroll ile geçiş
- Navigasyon: alt-orta sabit bar (dots + ok tuşları + sayaç)
- Keyboard: ← → ile geçiş, touch/swipe destekli
- Her slide'da fade-in animasyonu (0.5s, staggered delay)
- Mobil uyumluluk önemli.

### Kartlar
- `.card` — Standart koyu kart
- `.card.card-accent` — Altın kenarlıklı öne çıkan kart
- Border-radius: 16px, padding: 28px

---

## 3. Slide Yapısı (11 Slide)

Her slide'ın header'ında sol: Tibexa logosu, sağ: slide etiketi.
Cover slide'da logolar yan yana: **Tibexa × [Müşteri]**

### Cover (numarasız)
- Etiket: `Gizli · [Müşteri] için hazırlandı`
- Üst başlık: `Pazar Genişleme Sistemi · [Ay] [Yıl]`
- Ana başlık: Müşteriye özel hook (ör. "ABD'de yeni satış kanalları açıyoruz.")
- Alt başlık: Kısa operasyon tanımı
- Meta: Hazırlayan / Tarih / Kapsam
- Logolar: Sol üstte Tibexa × Müşteri

### 01 / Fırsat
- Pazar büyüklüğü ve müşterinin pozisyonu
- Hedeflenebilir segment'ler (pill formatında)
- Stat kartları: TAM (toplam erişilebilir pazar), ulaşılabilir karar verici sayısı

### 02 / Metodoloji
- "Şans değil, sistem." başlığı
- Timeline: Hafta hafta iş akışı (liste → segmentasyon → operasyon → raporlama)
- Varyasyon mantığı kartı
- Beklenen dönüş oranı kartı

### 03 / Yöntem A — Tek Kanallı Erişim Operasyonu
- Aktif kanal: Sadece Email
- Operasyonel tablo (fiyatsız): Ölçek / Hedef Kişi / Toplam Temas / Süre / Pipeline Görüşme
- 3 tier: Muhafazakar → Başlangıç (önerilen) → Büyüme
- **Fiyat bu slide'da gösterilmez**

### 04 / Yöntem B — Çok Kanallı Erişim Operasyonu
- Aktif kanallar: Email + LinkedIn + SMS/WhatsApp (tier bazlı)
- Aynı tablo yapısı, daha yüksek pipeline beklentisi
- "Neden çok kanal?" açıklama kartı
- **Fiyat bu slide'da gösterilmez**

### 05 / Karşılaştırma
- İki sütunlu kart: Yöntem A vs Yöntem B
- Karşılaştırma kriterleri: Kanallar / Kurulum hızı / Sistem karmaşıklığı / Pipeline görüşme / İdeal durum
- **Fiyat gösterilmez** — sadece operasyonel farklar
- Öneri kartı: "Yöntem A ile başlayıp geçiş yapılabilir"

### 06 / Müşteri Değeri
- **LTV (Lifetime Value) hesabı:** İlk sipariş → yıllık tekrar oranı → 3 yıllık birikim
- **SVG bar chart:** LTV birikimi yıl bazlı (İlk sipariş → Yıl 1 → Yıl 2 → Yıl 3)
- "Neden iki ürün grubu birlikte?" açıklama kartı
- Çarpan etkisi metrikleri: 1 Decision Maker → 2 Ürün Teklifi → 2x Pipeline

### 07 / Neden Tibexa
- "Sonuç ürettiğimizi kanıtladık." başlığı
- 3 kanıt kartı (sektör deneyimi / veri odaklı segmentasyon / aktif operasyon tecrübesi)
- Referans markalar (tag formatında)
- Çalışma prensibi kartı: "Partner olarak görüyoruz"

### 08 / Fiyatlandırma (Fiyat Matrisi)
- **Fiyat sadece bu slide'da gösterilir** — sunum boyunca değer ve operasyon anlatılır, fiyat en sona bırakılır
- 2 sütunlu matris: Yöntem A / Yöntem B
- 3 satır: Muhafazakar / Başlangıç (önerilen) / Büyüme
- Hedef kişi "× 2" notasyonuyla (2 ürün grubu)
- Her hücrede: Normal fiyat + Peşin fiyat
- Alt kartlar: Yöntem açıklamaları

### 09 / ROI Hesaplayıcı
- İnteraktif hesaplayıcı (JavaScript)
- Tab: Yöntem A / Yöntem B
- 4 girdi: Yatırım tutarı / Hedeflenen görüşme / Close rate / Ort. sözleşme tutarı
- 4 sonuç kartı: Kapanan anlaşma / Toplam gelir / Net kazanç / ROI çarpanı
- Görsel barlar: Yatırım vs Gelir karşılaştırması
- Renk kodlaması: 3x+ yeşil, 1-3x altın, <1x kırmızı

### 10 / Sonraki Adımlar
- Logolar: Tibexa × Müşteri (ortada, büyük)
- "Birlikte başlayalım."
- 3 karar sorusu: Hangi yöntem? / Hangi ürün önce? / Satış öncesi etkileşim?
- **CTA butonu konmaz** — sunum canlı yapılır, aksiyon sözlü alınır

---

## 4. Dil Kuralları

### Yapılacaklar
- **Operatör dili kullan:** "Pipeline operasyonu", "Pazar genişleme sistemi", "Erişim operasyonu"
- **Mevcut iş durumuna saygı göster:** Müşterinin zaten satışları varsa "satacağız" deme, "yeni kanallar açıyoruz" de
- **Hibrit dil:** Pipeline, close rate, decision maker gibi yerleşik terimler İngilizce kalır
- **"Yöntem" de, "Senaryo" deme:** Senaryo fiyat matrisinde fazla tekrar eder, dikkat dağıtır
- **Değer önce, fiyat sonra:** Sunum boyunca operasyon ve müşteri değeri anlatılır, fiyat en son slide'da verilir

### Yapılmayacaklar
- ~~Cold email~~ → "Erişim operasyonu" veya sadece "Email"
- ~~Outbound~~ → "Pazar genişleme" veya "Erişim"
- ~~Kampanya~~ → "Operasyon"
- ~~Lead generation~~ → "Pipeline oluşturma"
- ~~"[Müşteri]'yi satacağız"~~ → "[Müşteri]'ye yeni kanallar açıyoruz"
- ~~SMS + WhatsApp~~ → "SMS/WhatsApp" (tek kalem)

---

## 5. Fiyatlandırma Mantığı

### Matris Yapısı
- **Satırlar (ölçek):** Muhafazakar (1K) / Başlangıç (5K, önerilen) / Büyüme (10K)
- **Sütunlar (yöntem):** Yöntem A (tek kanallı) / Yöntem B (çok kanallı)
- Tüm fiyatlar **2 ürün grubu** üzerinden gösterilir (hedef: "5K × 2" notasyonu)
- Her hücrede normal fiyat + peşin fiyat


### Yöntem B Fiyatlandırma
- Yöntem A'nın yaklaşık 2x'i (çok kanal altyapı maliyeti)
- Muhafazakar tier'de oran daha düşük (~1.9x), büyüme tier'inde daha yüksek (~2.1x)

---

## 6. Yeni Teklif Oluşturma Checklist

1. **Müşteri logosu:** Beyaz/transparan versiyonu oluştur, `teklif/` klasörüne kaydet
2. **orzax.html'i kopyala:** `teklif/[musteri].html` olarak
3. **Başlık ve meta:** Title tag, cover label, "Gizli · [Müşteri] için hazırlandı"
4. **Cover hook:** Müşteriye özel ana başlık yaz
5. **Fırsat slide'ı:** Müşterinin sektörü ve pazarına göre özelleştir
6. **Segment pill'leri:** Hedeflenecek segmentleri güncelle
7. **Metodoloji:** Varyasyon mantığını müşteriye göre uyarla
8. **Yöntem tabloları:** Pipeline görüşme beklentilerini sektöre göre ayarla
9. **Müşteri Değeri:** LTV hesabını müşterinin sektörüne göre güncelle (ort. sipariş, tekrar oranı)
10. **Neden Tibexa:** Sektör deneyimini müşteriye uygun referanslarla destekle
11. **Fiyat matrisi:** Fiyatları güncelle
12. **ROI varsayılanları:** JS'teki scenario objelerini güncelle
13. **Sonraki Adımlar:** Karar sorularını müşteriye göre uyarla
14. **robots.txt:** Zaten `/teklif/` disallow — ek işlem gerekmez
15. **Deploy et, URL'yi müşteriye gönder**

---

## 7. Teknik Notlar

- **Font:** Google Fonts CDN'den yükleniyor (Red Hat Display)
- **Görseller:** Logolar PNG (transparan), grafikler inline SVG
- **Base64 kullanma:** Dosya boyutunu şişirir. Logoları ayrı dosya olarak tut.
- **JS:** Vanilla JS, framework yok. Slide navigasyonu + ROI hesaplayıcı.
- **Responsive:** Slide sistemi masaüstü sunumu için optimize. Mobilde scroll sorunlu olabilir — teklif masaüstünde/projektörde sunulur.
