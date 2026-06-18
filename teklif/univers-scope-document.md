# Ünverler Makine ERP — Detaylı Scope Document
## 3 Paket: Kapsam, Kapsam Dışı, Bağımlılıklar, Effort & Termin

> Kaynak: univers-veri-modeli.md + univers-ekran-envanteri.md
> Hazırlayan: Tibexa
> Tarih: 2026-05-04

---

## GENEL MİMARİ KARARLARI (Tüm Paketler İçin Geçerli)

| Karar | Tercih | Gerekçe |
|-------|--------|---------|
| Platform | Web tabanlı (SPA) | Ofis + atölye + TV ekranı, kurulum gerektirmez |
| Veritabanı | PostgreSQL | Relational, JSON desteği, formül alanları için esnek |
| ETA bağlantısı | SQL Server read (periyodik) + write (event bazlı) | API yok, doğrudan DB erişimi |
| Kimlik doğrulama | Kullanıcı adı + şifre, rol bazlı yetkilendirme | Basit, AD entegrasyonu gerekmez |
| Barkod | Web kamera veya USB barkod okuyucu (HTML5 API) | Ek donanım maliyeti yok |
| PDF | Server-side PDF üretimi, şablon motoruyla | Çok dilli, çok tipli form desteği |
| Hosting | On-premise veya cloud (müşteri tercihi) | ETA sunucusuna erişim gerekli |

---

# PAKET 1 — Satış & Teklif Yönetimi

## Özet

Ünverler Makine'nin **birinci önceliği**. Müşteriden teklif talebi geldiği andan sipariş onayına kadar olan tüm süreci dijitalleştirir. Şu an Excel + mail + telefon ile yürüyen teklif hazırlama, fiyatlandırma, müşteri takibi ve belge üretimi süreçlerini tek bir platforma taşır.

## Kapsam

### Ekranlar (11 adet)

| # | Ekran | Açıklama |
|---|-------|----------|
| E01 | Proje Listesi | Tüm projelerin filtrelenebilir ana listesi, durum renkleri |
| E02 | Proje Detay & Kalem Yönetimi | Tek projenin tüm kalemleri, toplamlar, alt kalemler |
| E03 | Kalem Detay & Versiyon Zinciri | Ölçüler, malzeme listeleri, versiyon timeline, diff |
| E04 | Malzeme Listesi Düzenleme | Tasarımcı + satın almacı ortak çalışma ekranı |
| E05 | Fiyatlandırma Çalışması | 3 yöntem, geçmiş karşılaştırma, karar |
| E06 | PDF Oluştur & Gönder | Çok dilli/tipli belge üretimi, mail |
| E07 | Proje Takip Tablosu | Workflow board — tick bazlı ilerleme |
| E08 | Admin Formül Yönetimi | Hacim/talaş/süre formülleri, çarpanlar |
| E09 | Firma Yönetimi | Müşteri bilgileri, geçmiş |
| E10 | Sipariş Onay Döngüsü | Bekleyen teklifler, uyarılar, fiyat müzakeresi |
| E11 | Yönetim Dashboard (Temel) | Satış hunisi, dikkat gerektiren, dönem özeti |

### Entity'ler (Bu pakette oluşturulacak)

| Entity | Kayıt Hacmi (Yıl) | Notlar |
|--------|--------------------|--------|
| Firma | ~100 | Temel müşteri verileri |
| Proje | ~500 | Talep/teklif ana kaydı |
| Kalem | ~2000 | Proje alt kalemleri, montaj numaraları |
| BoyutParametreleri | ~2000 | 6 ölçü kutucuğu (temiz+ham) |
| AdminFormülleri | ~50 | Sabit tanımlar, az değişir |
| MalzemeListesi | ~5000 | UTA/USA, versiyon zinciri |
| MalzemeKalemi | ~30000 | BOM satırları |
| MaddeKartı | ~2000 | ETA'dan çekilecek (temel altyapı) |
| FiyatlandırmaÇalışması | ~2000 | 3 yöntem hesaplaması |
| ProjeTakipAdımları | ~28000 | Kalem × 14 workflow adımı |
| Kullanıcı | ~20 | Roller + erişim |
| PDFŞablonu | ~10 | Statik şablon tanımları |

### Fonksiyonlar

| # | Fonksiyon | Detay |
|---|-----------|-------|
| F01 | Proje oluşturma & düzenleme | Otomatik P numarası, firma seçimi, çoklu kalem |
| F02 | Kalem yönetimi | Ekleme, silme, durum değiştirme, kısmi sevk takibi |
| F03 | Versiyon zinciri | Yeni versiyon açma, kilitleme, aşama geçişi, diff |
| F04 | Malzeme listesi girişi | Tasarımcı ölçü + malzeme, SA fiyat + ham ölçü |
| F05 | Madde kartından fiyat çekme | Madde kodu → otomatik fiyat (imalat: hacim×kg, keçe/standart: birim) |
| F06 | Formül motoru | Admin tanımlı formüllerle hacim, talaş, süre hesaplama |
| F07 | Fiyatlandırma 3 yöntem | Çarpan, hacim, süre bazlı — geçmiş projelerle karşılaştırma |
| F08 | PDF üretimi | 4-5 şablon × 2-3 dil, naming convention, havuza kayıt |
| F09 | Mail gönderimi | SMTP ile PDF ekli mail (opsiyonel, Outlook trigger alternatif) |
| F10 | Workflow takibi | Tick bazlı otomatik tarih, adım ilerlemesi |
| F11 | Sipariş onay döngüsü | Bekleme süresi takibi, 1 hafta uyarı, anlaşma fiyatı |
| F12 | Temel dashboard | Satış hunisi, dikkat gerektiren, dönem özeti |
| F13 | Rol bazlı erişim | 4 rol (YÖN, PM, SAT, TAS + SA sınırlı), ekran/alan bazlı |
| F14 | ETA madde kartı senkronizasyonu | Periyodik SQL çekme (temel altyapı) |

### Kapsam Dışı (Paket 1'de YOK)

- Satın alma sipariş verme ve takibi (Paket 2)
- Malzeme geliş/gidiş takibi (Paket 2)
- Fason iş yönetimi (Paket 2)
- İş emri oluşturma ve proses yönetimi (Paket 3)
- Tezgah/istasyon ekranları, barkod başla/bitir (Paket 3)
- Üretim planlama, Gantt (Paket 3)
- Gerçek maliyet analizi (Paket 3)
- ETA'ya sipariş aktarımı (Paket 2)
- Fatura kesme/takip (ETA'da kalır)
- IoT / tezgah entegrasyonu (gelecek)
- Mobil uygulama (gelecek)

### Bağımlılıklar

| Bağımlılık | Kimden | Açıklama |
|------------|--------|----------|
| ETA sunucu erişimi | Ünverler Makine IT / ETA | SQL bağlantı bilgileri, madde kartı tablo yapısı |
| PDF şablon tasarımı | Ünverler Makine | Mevcut teklif/sipariş form örnekleri (4-5 tip × 2-3 dil) |
| Tip kodu listesi | Ünverler Makine (Mert) | HS1K, HS4K vb. ~15 adet tip kodu ve açıklamaları |
| Geçmiş proje verileri | Ünverler Makine | Excel'lerden migration yapılacaksa mevcut verilerin temizlenmesi |
| Formül tanımları | Ünverler Makine (Mert) | Hacim, talaş, süre hesaplama formüllerinin detaylı dökümü |
| Sunucu / hosting kararı | Ünverler Makine | On-premise mi, cloud mu |

### Teslimat Planı

| Hafta | Milestone | Çıktı |
|-------|-----------|-------|
| 1-2 | Altyapı & Veri Modeli | DB şeması, auth sistemi, temel UI framework, E09 (Firma) |
| 3-4 | Proje & Kalem Çekirdeği | E01, E02, E03 (versiyon zinciri dahil) |
| 5-6 | Malzeme & Fiyatlandırma | E04, E05, E08 (formül motoru) |
| 7-8 | Belge Üretimi & Workflow | E06 (PDF), E07 (takip tablosu), E10 (sipariş döngüsü) |
| 9 | Dashboard & Entegrasyon | E11, ETA madde kartı sync, rol bazlı erişim |
| 10 | Test & Devreye Alma | UAT, veri migration, eğitim, go-live |

**Toplam: ~10 hafta**

---

# PAKET 2 — Satın Alma & Tedarik Zinciri

## Özet

Paket 1'de oluşan sipariş verisinin satın alma sürecine akmasını sağlar. Tasarımcının "şu malzemeleri al" demesinden, satın almacının firmalardan teklif alıp sipariş vermesine, malzemenin gelip depoya girmesine kadar olan döngüyü kapsar. Fason iş takibi de bu pakette.

## Ön Koşul

**Paket 1 tamamlanmış olmalıdır.** Paket 2, Paket 1'deki Kalem, MalzemeListesi, MalzemeKalemi ve MaddeKartı entity'lerinin üzerine inşa edilir.

## Kapsam

### Ekranlar (6 adet)

| # | Ekran | Açıklama |
|---|-------|----------|
| E12 | Satın Alma Talep Ekranı | Tasarım/üretimden gelen taleplerin yönetimi |
| E13 | Satın Alma Sipariş Takibi | Firmalardan alınan malzemelerin durumu |
| E14 | Malzeme Durum Ekranı (Ofis) | Proje bazlı malzeme checklist — fiyat dahil |
| E15 | Malzeme Durum Ekranı (Atölye) | E14'ün sadeleştirilmiş, fiyatsız versiyonu |
| E16 | Fason İş Takibi | Dışarıya gönderilen işlerin yönetimi |
| E17 | Madde Kartı Yönetimi | ETA sync, eksik kontrol, fiyat güncelleme |

### Entity'ler (Bu pakette oluşturulacak)

| Entity | Kayıt Hacmi (Yıl) | Notlar |
|--------|--------------------|--------|
| SatınAlmaTalebi | ~5000 | Proje + genel + sarf talepleri |
| SatınAlmaSiparişi | ~5000 | Firmalardan alım |
| FasonİşTakibi | ~500 | Dışarıya giden işler |

**Paket 1'den devralınan entity'ler:** MalzemeKalemi (genişletilir), MaddeKartı (tam kullanıma alınır), Kalem (durum güncellemeleri)

### Fonksiyonlar

| # | Fonksiyon | Detay |
|---|-----------|-------|
| F15 | Otomatik talep oluşturma | USA kilitlendiğinde → satın alma talepleri otomatik düşer |
| F16 | Genel talep girişi | Üretim/operatörden proje dışı talepler (sarf, elmas vb.) |
| F17 | Sipariş oluşturma & takip | Firma seç, fiyat gir, hedef tarih, durum takibi |
| F18 | Malzeme geldi işaretleme | Kısmi/tam geldi, tarih, otomatik durum güncelleme |
| F19 | Montaj hazırlık kontrolü | Tüm malzemeler geldi mi → montaja hazır durumu |
| F20 | Fason gönderim & dönüş | İş emri → fasona gönder → dönüş işaretle |
| F21 | Hedef tarih aşım uyarıları | Renk sistemi: kırmızıya dönen siparişler |
| F22 | ETA sipariş aktarımı | Onaylanan siparişleri ETA'ya yazma (fatura için) |
| F23 | Madde kartı tam yönetimi | Eksik kart tespiti, fiyat güncelleme periyodu |
| F24 | Atölye erişim modu | Fiyatsız görünüm, montaj no / firma ile sorgulama |

### Kapsam Dışı (Paket 2'de YOK)

- İş emri oluşturma (Paket 3 — ama satın alma talebi iş emrini tetikleyecek altyapı hazırlanır)
- Tezgah/barkod sistemi (Paket 3)
- Üretim planlama (Paket 3)
- Gerçek maliyet hesaplama (Paket 3)
- Fatura kesme (ETA'da kalır)
- Tedarikçi değerlendirme / puanlama (gelecek)

### Bağımlılıklar

| Bağımlılık | Kimden | Açıklama |
|------------|--------|----------|
| Paket 1 canlıda | Tibexa | Kalem, MalzemeListesi, MaddeKartı entity'leri hazır |
| ETA yazma erişimi | Ünverler Makine IT / ETA | Sipariş aktarımı için INSERT/UPDATE yetkisi |
| ETA tablo yapısı | Ünverler Makine IT / ETA | Sipariş, fatura tablolarının şeması (toplantı gerekli) |
| Tedarikçi listesi | Ünverler Makine (SA) | Sık kullanılan firmalar, malzeme-firma eşleştirmeleri |
| Fason firma listesi | Ünverler Makine (FAS) | Fasoncu firmalar ve iş tipleri |

### Teslimat Planı

| Hafta | Milestone | Çıktı |
|-------|-----------|-------|
| 1-2 | Talep & Sipariş Altyapısı | E12, E13, entity'ler, otomatik talep akışı |
| 3-4 | Malzeme Durum & ETA | E14, E15, E17, ETA yazma entegrasyonu |
| 5 | Fason & Finalizasyon | E16, montaj hazırlık kontrolü |
| 6 | Test & Devreye Alma | UAT, eğitim, go-live |

**Toplam: ~6 hafta**

---

# PAKET 3 — Üretim & İstasyon Yönetimi

## Özet

Üretim katının dijitalleştirilmesi. Proses paketlerinin tanımlanması, iş emirlerinin oluşturulması, tezgah operatörlerinin barkod ile iş başlatıp bitirmesi, üretim ilerlemesinin matris ve timeline olarak takibi. İleride gerçek maliyet analizinin yapılabilmesi için altyapı da bu pakette.

## Ön Koşul

**Paket 1 + Paket 2 tamamlanmış olmalıdır.** Paket 3, satın alma durum verisi (malzeme geldi mi) ve malzeme listesi verisini kullanır.

## Kapsam

### Ekranlar (7 adet)

| # | Ekran | Açıklama |
|---|-------|----------|
| E18 | Proses Paket Yönetimi | TKP şablonları: adımlar, sıralar, süreler |
| E19 | İş Emri Oluşturma | Malzeme + proses paketi → iş emirleri |
| E20 | İstasyon Ekranı (Tezgah) | Barkod başla/bitir, operatör arayüzü |
| E21 | Üretim Durumu Matrisi | İstasyon × parça matris görünümü, renk sistemi |
| E22 | Üretim Planlama (Gantt) | Zaman çizelgesi, çakışma kontrolü |
| E23 | Gerçek Maliyet Analizi | Teklif vs gerçek, süre vs teorik |
| E24 | Gelişmiş Yönetim Dashboard | E11 + üretim + maliyet + tip/firma analiz |

### Entity'ler (Bu pakette oluşturulacak)

| Entity | Kayıt Hacmi (Yıl) | Notlar |
|--------|--------------------|--------|
| ProsesPaketi | ~30 | Şablon tanımları, az değişir |
| ProsesAdımı | ~200 | Paket × 5-8 adım |
| İşEmri | ~20000 | Kalem × malzeme × proses adım |

**Paket 1-2'den devralınan:** Kalem (durum), MalzemeKalemi, SatınAlmaSiparişi (geldi mi), FasonİşTakibi, BoyutParametreleri (teorik süre)

### Fonksiyonlar

| # | Fonksiyon | Detay |
|---|-----------|-------|
| F25 | Proses paketi tanımlama | TKP oluştur, adım ekle/çıkar/sırala, fason işaretle |
| F26 | İş emri oluşturma | Paketten otomatik + manuel düzenleme |
| F27 | Bağımlılık motoru | Önceki adım + malzeme durumu → yapılabilirlik hesabı |
| F28 | Barkod başla/bitir | Web kamera veya USB okuyucu, zaman damgası |
| F29 | Kısmi tamamlama | 4 adetten 2'sini yaptım, 2 kaldı |
| F30 | İstasyon filtreleme | Operatör sadece kendi tezgahını görür |
| F31 | Renk sistemi | Yeşil/sarı/mavi/kırmızı otomatik hesaplama |
| F32 | Neden bekliyor | Beklemedeki işe açıklama girişi |
| F33 | Üretim matrisi | Parça × istasyon grid, canlı durum |
| F34 | Gantt planlama | İş emirlerinin zaman çizelgesi, termin çizgisi |
| F35 | Gerçek süre hesaplama | Başla-bitir arasındaki süre vs teorik süre |
| F36 | Gerçek maliyet raporu | Malzeme + işçilik gerçek maliyet vs teklif fiyatı |
| F37 | Gelişmiş dashboard | Üretim metrikleri, istasyon doluluk, tip/firma analiz, kârlılık trendi |
| F38 | Duruş kodu altyapısı | Tablo yapısı hazır, UI gelecekte (elmas, setup, arıza) |
| F39 | Tezgah ID altyapısı | İstasyon entity'sine tezgah_id alanı (IoT gelecekte) |

### Kapsam Dışı (Paket 3'te YOK)

- Duruş kodları UI (altyapısı hazır, ekran gelecekte)
- IoT tezgah entegrasyonu (altyapı bırakılır, sensör bağlantısı gelecekte)
- Metot süresi vs gerçek süre detaylı karşılaştırma UI (veri toplanır, analiz ekranı gelecekte)
- Bakım/arıza yönetimi (gelecek)
- Kalite kontrol detay modülü (gelecek)
- Depo/stok yönetimi (gelecek)
- Mobil operatör uygulaması (gelecek)

### Bağımlılıklar

| Bağımlılık | Kimden | Açıklama |
|------------|--------|----------|
| Paket 1 + 2 canlıda | Tibexa | Tüm temel entity'ler hazır |
| Proses paket tanımları | Ünverler Makine (Mert/ÜS) | ~15-30 TKP'nin adım adım dökümü |
| Atölye donanımı | Ünverler Makine | Her istasyona bilgisayar/tablet, barkod okuyucu |
| Barkod standardı | Ünverler Makine (TAS) | Teknik resimlerdeki barkod formatı (montaj no encoding) |
| İstasyon listesi | Ünverler Makine (ÜS) | Tezgah isimleri, sayıları, grupları |
| Maliyet parametreleri | Ünverler Makine (YÖN) | Saat ücreti / gün ücreti tanımları (gerçek maliyet için) |

### Teslimat Planı

| Hafta | Milestone | Çıktı |
|-------|-----------|-------|
| 1-2 | Proses & İş Emri | E18, E19, bağımlılık motoru |
| 3-4 | Tezgah & İstasyon | E20 (barkod), E21 (matris), renk sistemi |
| 5-6 | Planlama & Analiz | E22 (Gantt), E23 (maliyet), E24 (dashboard) |
| 7 | Atölye Pilot | Atölye donanım kurulumu, pilot istasyonlarda test |
| 8 | Test & Devreye Alma | UAT, eğitim, go-live |

**Toplam: ~8 hafta**

---

# PAKETLER ARASI İLİŞKİ

```
┌──────────────────────────────────────┐
│         PAKET 1 (10 hafta)           │
│     Satış & Teklif Yönetimi          │
│                                      │
│  Proje → Kalem → Malzeme Listesi     │
│  Versiyon Zinciri → Fiyatlandırma    │
│  PDF → Workflow → Dashboard          │
│                                      │
│  ★ Tek başına değer üretir           │
│  ★ Diğer paketlerin temeli           │
└──────────────┬───────────────────────┘
               │ Veri akışı: Kalem, MalzemeKalemi, 
               │ MaddeKartı, sipariş onayı
               ▼
┌──────────────────────────────────────┐
│         PAKET 2 (6 hafta)            │
│     Satın Alma & Tedarik Zinciri     │
│                                      │
│  Talep → Sipariş → Geldi/Gelmedi     │
│  Fason → ETA Entegrasyonu            │
│  Malzeme Durum (Ofis + Atölye)       │
│                                      │
│  ★ Paket 1 olmadan çalışamaz         │
│  ★ Paket 3'ü besler (malzeme durumu) │
└──────────────┬───────────────────────┘
               │ Veri akışı: Malzeme geldi mi,
               │ fason durumu, montaj hazırlık
               ▼
┌──────────────────────────────────────┐
│         PAKET 3 (8 hafta)            │
│     Üretim & İstasyon Yönetimi       │
│                                      │
│  Proses Paketi → İş Emri → Barkod   │
│  Matris → Gantt → Gerçek Maliyet     │
│  Gelişmiş Dashboard                  │
│                                      │
│  ★ Paket 1+2 olmadan çalışamaz       │
│  ★ Gelecek genişlemelerin temeli      │
└──────────────────────────────────────┘
```

---

# TOPLAM PROJE ÖZETİ

## Sayılarla

| Metrik | Paket 1 | Paket 2 | Paket 3 | Toplam |
|--------|---------|---------|---------|--------|
| Ekran sayısı | 11 | 6 | 7 | **24** |
| Fonksiyon sayısı | 14 | 10 | 15 | **39** |
| Entity sayısı (yeni) | 12 | 3 | 3 | **18** |
| Tahmini süre | 10 hafta | 6 hafta | 8 hafta | **24 hafta** |
| Reusable component | 10 (tümü burada) | 0 (Paket 1'den devralır) | 0 (devralır) | **10** |

## Sıralı vs Paralel

**Sıralı teslimat (önerilen):** 10 + 6 + 8 = **24 hafta** (~6 ay)
- En düşük risk, her paket kendi başına değer üretir
- Paket 1 canlıyken Paket 2 geliştirilir

**Kısmen paralel:** Paket 2 altyapısı Paket 1'in 7. haftasında başlayabilir → **~20 hafta** (~5 ay)
- Orta risk, koordinasyon gerekir

**Tam paralel:** Mümkün değil — Paket 2 ve 3, Paket 1'in entity'lerine bağımlı.

## Senaryo Alternatifleri

### Senaryo A: Sadece Paket 1
- Süre: 10 hafta
- Değer: Excel'den kurtuluş, teklif süreci %80 dijital
- Kim mutlu olur: PM, SAT, YÖN
- Kim hâlâ Excel'de: SA, ÜS, OP

### Senaryo B: Paket 1 + Paket 2
- Süre: ~16 hafta (sıralı) veya ~14 hafta (kısmen paralel)
- Değer: Teklif + satın alma dijital, malzeme takibi otomatik
- Kim mutlu olur: PM, SAT, SA, YÖN, TAS
- Kim hâlâ Excel'de: ÜS, OP (ama atölyede malzeme durumu görünür)

### Senaryo C: Paket 1 + 2 + 3 (Tam kapsam)
- Süre: ~24 hafta (sıralı) veya ~20 hafta (kısmen paralel)
- Değer: Uçtan uca dijital, gerçek maliyet takibi
- Kim mutlu olur: Herkes
- Kalan: Duruş kodları detayı, IoT, mobil (gelecek)

---

# VERİ MİGRASYONU

Ünverler Makine'nin mevcut Excel'lerinden aktarılması gereken veriler:

| Veri | Kaynak | Hedef | Öncelik |
|------|--------|-------|---------|
| Geçmiş projeler & kalemler | Master Excel | Proje + Kalem | Yüksek (fiyatlandırma referansı için) |
| Tip kodları & tanımlar | Manuel liste | Enum/Lookup | Yüksek |
| Madde kartları | ETA SQL | MaddeKartı | Yüksek |
| Firma listesi | Excel/ETA | Firma | Yüksek |
| Geçmiş fiyatlar | Teklif Excel'leri | FiyatlandırmaÇalışması | Orta (geçmiş karşılaştırma için) |
| Proses paketleri | Manuel (Mert ile çalışma) | ProsesPaketi | Paket 3'te |

**Kritik not:** Geçmiş proje verileri fiyatlandırma referansı için şart. "Geriye dönük 100 projeyi de görebiliriz" (55:11). Paket 1 öncesinde data temizleme çalışması yapılmalı.

---

# RİSK MATRİSİ

| Risk | Olasılık | Etki | Azaltma |
|------|----------|------|---------|
| ETA SQL erişimi sorunlu | Orta | Yüksek | Erken toplantı (Paket 1, Hafta 1), fallback: CSV import |
| Formül karmaşıklığı beklenenden fazla | Düşük | Orta | MVP formüllerle başla, admin ekranıyla iterasyon |
| Geçmiş veri kalitesi düşük | Yüksek | Orta | Veri temizleme sprint'i, eksik=manuel giriş |
| Atölye adaptasyonu düşük | Orta | Yüksek (Paket 3) | Pilot istasyon, kolay UX, büyük butonlar |
| Kapsam genişlemesi | Yüksek | Yüksek | Paket sınırları net, ek talepler yeni paket/CR |
| Mevcut Excel alışkanlıkları | Yüksek | Orta | Paralel çalışma dönemi, zorunlu geçiş tarihi |

---

# TOPLANTI GEREKLİLİKLERİ (Paket 1 Başlamadan Önce)

| # | Toplantı | Katılımcı | Süre | Çıktı |
|---|----------|-----------|------|-------|
| 1 | ETA Entegrasyon | Ünverler Makine IT + ETA + Tibexa | 2 saat | SQL erişim, tablo yapıları, okuma/yazma scope |
| 2 | Formül Detaylandırma | Mert + Tibexa | 1.5 saat | Tüm formüllerin matematiksel dökümü |
| 3 | PDF Şablon İnceleme | Mert/SAT + Tibexa | 1 saat | 4-5 form örneği, alan eşleştirmesi |
| 4 | Geçmiş Veri İnceleme | Mert + Tibexa | 1.5 saat | Excel'lerin yapısı, migration planı |
| 5 | Tip Kodu & Proses Tanımlama | Mert/ÜS + Tibexa | 1 saat | ~15 tip kodu, ~15-30 TKP tanımı |

---

*Bu scope document, veri modeli (univers-veri-modeli.md) ve ekran envanteri (univers-ekran-envanteri.md) ile birebir uyumludur. Tüm ekran numaraları (E01-E24) ve fonksiyon numaraları (F01-F39) bu dokümanlara referans verir.*
