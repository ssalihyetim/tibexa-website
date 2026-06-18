# Ünverler Makine ERP — Ekran Envanteri & Kullanıcı Akışları
## Toplantıdan Çıkarılan Tüm Ekranlar, Roller ve Akışlar

> Kaynak: UniversMeetingTscrip.md + univers-veri-modeli.md
> Hazırlayan: Tibexa

---

## 1. ROLLER VE ERİŞİM MATRİSİ

| Rol | Kısaltma | Kişi Sayısı (Tahmin) | Ana Sorumluluk |
|-----|----------|---------------------|----------------|
| Yönetim | YÖN | 2 | Dashboard, karar, onay |
| Proje Müdürü | PM | 2-3 | Teklif, sipariş, proje takip, fiyatlandırma |
| Satışçı | SAT | 2-3 | Teklif formu, müşteri iletişimi |
| Tasarımcı (AR-GE) | TAS | 2-3 | Malzeme listesi, ölçü girişi, proses tanımlama |
| Satın Almacı | SA | 2-3 | Fiyat girişi, sipariş takibi, malzeme durumu |
| Üretim Sorumlusu | ÜS | 1-2 | Planlama, istasyon yönetimi, iş emri |
| Operatör (Tezgah) | OP | 5-10 | Barkod başla/bitir, malzeme sorgulama |
| Muhasebe | MUH | 1-2 | Fatura, vade, ödeme takibi, ETA |
| Fason Takip | FAS | 1 | Dış iş takibi |

---

## 2. EKRAN KATALOĞU

### PAKET 1 — Satış & Teklif Çekirdeği

---

#### E01 — Proje Listesi (Ana Ekran)

**Kullananlar:** PM, SAT, YÖN
**Amaç:** Tüm projelerin/taleplerin tek bakışta görülmesi, filtrelenebilir liste.

| Bileşen | Detay |
|---------|-------|
| Tablo sütunları | Proje No (P-xxx), Firma Adı, Talep Tarihi, Kalem Sayısı, Toplam Tutar, Para Birimi, Durum, Son İşlem Tarihi |
| Filtreler | Durum (açık/beklemede/onaylı/iptal), Firma, Tarih aralığı, Para birimi |
| Sıralama | Tarih, tutar, firma adı |
| Renk kodları | Açık=mavi, Beklemede=turuncu, 1+ hafta cevapsız=kırmızı, Onaylı=yeşil, İptal=gri |
| Aksiyonlar | Yeni Proje (+), Projeye Git, Hızlı Durum Değiştir |
| Beslenen entity | Proje, Firma, Kalem (count) |

**Toplantı referansı:** "Bu tekliflerin ana bilgilerini tuttuğumuz ayrı bir kit" (07:37), "Bir haftayı geçti, kırmızı yansın" (57:18)

---

#### E02 — Proje Detay & Kalem Yönetimi

**Kullananlar:** PM, SAT
**Amaç:** Tek bir projenin tüm kalemleriyle birlikte yönetilmesi.

| Bileşen | Detay |
|---------|-------|
| Üst bölüm — Proje Başlığı | Proje No, Firma, Talep Tarihi, Ödeme Koşulları, Para Birimi, Dil, Form Tipi, Muhasebe Onay durumu |
| Orta bölüm — Kalem Tablosu | Kalem No, Montaj No, Ürün Tanımı, Tip Kodu, Adet, Birim Fiyat, Toplam, Termin Tarihi, Termin Haftası, Durum, Sevk Durumu |
| Alt bölüm — Toplamlar | Ara Toplam, Nakliye/Paketleme, İskonto, KDV, Gümrük, Genel Toplam |
| Notlar paneli | Proje notları, geçmiş açıklamalar |
| İlişkili projeler | Aynı firma + aynı tip kodundaki geçmiş projeler (linkli) |
| Aksiyonlar | Kalem Ekle, Kalem Sil, PDF Oluştur, Teklif Gönder, Sipariş Onayla, Durumu Güncelle |
| Beslenen entity | Proje, Kalem, Firma, ProjeTakipAdımları |

**Toplantı referansı:** "Talep numarası, ürün tanımı, ebat, fiyat... hepsi burada" (13:22), "Uyguru nakliye, paketleme, iskonto, KDV, gümrük" (05:07)

---

#### E03 — Kalem Detay & Versiyon Zinciri

**Kullananlar:** PM, TAS, SA
**Amaç:** Tek bir kalemin tam yaşam döngüsü — ölçüler, malzeme listeleri, fiyatlandırma, versiyon geçmişi.

| Bileşen | Detay |
|---------|-------|
| Üst bölüm — Kalem Bilgileri | Montaj No, Ürün Tanımı, Tip Kodu, Adet, Durum |
| Boyut Parametreleri kartı | Temiz ölçüler (dış çap, iç çap, boy) — TAS girer / Ham ölçüler — SA girer / Hesaplanan: hacim, talaş, teorik süre |
| Versiyon Zinciri timeline | v1 [teklif] → v2 [teklif] → v3 [sipariş]... her versiyon: tarih, kim, neden değişti, durum |
| Aktif Malzeme Listesi | Güncel versiyonun malzeme kalemleri (tablo) |
| Versiyon Diff | Herhangi iki versiyon seçip fark göster (eklenen/silinen/değişen satırlar) |
| Aksiyonlar | Yeni Versiyon Aç, Versiyonu Kilitle, Diff Göster, Fiyat Çalışması Aç |
| Beslenen entity | Kalem, BoyutParametreleri, MalzemeListesi, MalzemeKalemi |

**Toplantı referansı:** "Revizyon 1, 2 gibi tutulması gerekiyor" (32:36), "İlk halini bulmalı" (36:29), "İki aradaki farkı görebilelim" (34:11)

---

#### E04 — Malzeme Listesi Düzenleme

**Kullananlar:** TAS (ölçü/malzeme), SA (fiyat/ham ölçü)
**Amaç:** Bir versiyonun malzeme kalemlerinin girilmesi/düzenlenmesi.

| Bileşen | Detay |
|---------|-------|
| Versiyon başlığı | Kalem No, Versiyon, Aşama (teklif/sipariş), Durum |
| Malzeme tablosu | Sıra, Malzeme Grubu (imalat/keçe/standart/sarf), Madde Kodu (dropdown + arama), Tanım, Adet, Birim |
| Ölçü sütunları (TAS) | Temiz Dış Çap, Temiz İç Çap, Temiz Boy |
| Ölçü sütunları (SA) | Ham Dış Çap, Ham İç Çap, Ham Boy |
| Fiyat sütunları (SA) | Birim Fiyat, Fiyat Kaynağı (madde kartı/manuel/son alış), Toplam |
| Alt toplamlar | İmalat toplam, Keçe toplam, Standart toplam, Genel toplam |
| Aksiyonlar | Satır Ekle/Sil, Madde Kartından Fiyat Çek, Kaydet, Satın Almaya Gönder, Kilitle |
| Beslenen entity | MalzemeListesi, MalzemeKalemi, MaddeKartı |

**İş akışı:**
1. TAS malzemeleri ve temiz ölçüleri girer → Kaydet
2. SA'ya gönder butonu → SA'nın E04 ekranına düşer
3. SA ham ölçüleri ve fiyatları girer → Kaydet
4. PM fiyatlandırmaya geçer

**Toplantı referansı:** "Tasarım temiz ölçüleri oluşturuyor. Satın alma fiyatları giriyor." (24:15)

---

#### E05 — Fiyatlandırma Çalışması

**Kullananlar:** PM, YÖN
**Amaç:** Bir kalem için 3 farklı yöntemle fiyat hesaplayıp, geçmiş referanslarla karşılaştırıp karar vermek.

| Bileşen | Detay |
|---------|-------|
| Üst bölüm — Kalem özeti | Montaj No, Ürün Tanımı, Tip Kodu, Toplam Malzeme Fiyatı |
| Hesaplama kartları (yan yana) | |
| ├ Kart 1: Çarpan | Malzeme toplamı × seçilen çarpan = teklif fiyatı. Çarpan ayarlanabilir slider/input |
| ├ Kart 2: Hacim | Hesaplanan hacim × birim fiyat = teklif fiyatı |
| └ Kart 3: Süre | Teorik işleme süresi (gün) × gün ücreti = teklif fiyatı |
| Geçmiş projeler paneli | Aynı tip kodundaki geçmiş kalemler: Proje No, Firma, Tarih, Ölçüler, Çarpan, Fiyat. Sınırsız scroll. |
| Seçim alanı | Hangi yöntemi/fiyatı seçiyorum (radio) + Manuel override imkanı |
| Aksiyonlar | Fiyat Seç ve Kaleme Yaz, Karşılaştırmayı Kaydet |
| Beslenen entity | FiyatlandırmaÇalışması, Kalem, BoyutParametreleri, AdminFormülleri, (geçmiş) Kalem+Fiyat |

**Toplantı referansı:** "Bana 3 tane fiyat getirecek. Bir de eski teklifler göreceğim. Oradan karar vereceğim." (53:04), "Geriye dönük 100 projeyi de görebiliriz" (55:11)

---

#### E06 — PDF Oluştur & Gönder

**Kullananlar:** PM, SAT
**Amaç:** Teklif/proforma/sipariş onay formunu PDF olarak oluşturup kaydetmek veya mail ile göndermek.

| Bileşen | Detay |
|---------|-------|
| Şablon seçimi | Form tipi (teklif/proforma/sipariş onay) × Dil (TR/EN/DE) = dropdown |
| Önizleme | PDF önizleme paneli |
| Dosya adı | Otomatik: {ProjeNo}-{Firma}-{Tarih}-{Tip} — düzenlenebilir |
| Kayıt yeri | Sunucudaki havuz dizini |
| Mail gönderimi (opsiyonel) | Kime (firma email), Konu (şablondan), Gövde (şablondan), Ek: PDF |
| Aksiyonlar | Oluştur, Kaydet, Gönder, İndir |
| Beslenen entity | PDFŞablonu, Proje, Kalem, Firma |

**Toplantı referansı:** "PDF olarak kaydedip müşteriye mail atıyorum" (55:23), "Naming convention: sipariş numarası-müşteri-tarih" (10:49)

---

#### E07 — Proje Takip Tablosu (Workflow Board)

**Kullananlar:** PM, YÖN
**Amaç:** Bir projenin tüm kalemlerinin hangi aşamada olduğunu tek bakışta görmek.

| Bileşen | Detay |
|---------|-------|
| Satırlar | Her kalem bir satır |
| Sütunlar (adımlar) | Tasarım Başladı → Tasarım Bitti → SA Fiyat Girdi → Teklif Hazırlandı → Teklif Gönderildi → Sipariş Onaylandı → USA Başladı → USA Bitti → SA Talep → Üretim Başladı → Montaj → Kalite → Sevk → Fatura |
| Hücre içeriği | Tick (✓) + tarih + kim. Boşsa henüz yapılmamış. |
| Renk | Tick atılmış=yeşil, Sıradaki=turuncu highlight, Gecikmeli=kırmızı |
| Filtreler | Proje seçimi, sadece aktif kalemler, tarih aralığı |
| Beslenen entity | ProjeTakipAdımları, Kalem |

**Toplantı referansı:** "Tiklenecek, tarih otomatik gelecek" (45:37), "Proje takip çizelgesi" (45:37)

---

#### E08 — Admin Formül Yönetimi

**Kullananlar:** YÖN (sadece)
**Amaç:** Hacim, talaş, süre hesaplama formüllerini ve çarpanları yönetmek.

| Bileşen | Detay |
|---------|-------|
| Formül listesi | Formül Adı, İfade, Çarpan, Tip Kodu (varsa), Aktif/Pasif |
| Formül düzenleme | İfade editörü (değişkenler: temiz_dis_cap, ham_boy, vb.), test alanı (örnek değer gir → sonuç gör) |
| Çarpan yönetimi | Tip kodu bazlı varsayılan çarpanlar tablosu |
| Aksiyonlar | Ekle, Düzenle, Pasife Al, Test Et |
| Beslenen entity | AdminFormülleri |

**Toplantı referansı:** "Admin ekranı gibi. Hacim hesaplama şu formunda olacak" (28:10), "Admin değiştirebiliyor olmalı" (28:12)

---

#### E09 — Firma Yönetimi

**Kullananlar:** PM, SAT, YÖN
**Amaç:** Müşteri bilgilerini yönetmek, firma bazlı geçmişi görmek.

| Bileşen | Detay |
|---------|-------|
| Firma listesi | Firma Adı, Müşteri Kodu, Ülke, Proje Sayısı, Toplam Ciro |
| Firma detay | İletişim bilgileri, ödeme koşulları, para birimi, notlar |
| Firma geçmişi | Bu firmaya verilen tüm teklifler/siparişler (timeline) |
| Beslenen entity | Firma, Proje, Kalem |

---

#### E10 — Sipariş Onay Döngüsü

**Kullananlar:** PM, SAT
**Amaç:** Teklif gönderildikten sonra müşteriden dönüş takibi.

| Bileşen | Detay |
|---------|-------|
| Bekleyen teklifler listesi | Proje No, Firma, Gönderim Tarihi, Bekleme Süresi, Tutar |
| Uyarı sistemi | 1 hafta geçmiş = kırmızı satır (mail değil, ekranda renk) |
| Müşteri dönüşü | Onaylandı (tarih + anlaşma fiyatı gir) / İptal (tarih + neden gir) |
| Fiyat müzakeresi | Teklif fiyatı vs anlaşma fiyatı yan yana, fark göster |
| Aksiyonlar | Onayla, Reddet, Fiyat Güncelle, Sipariş Onay Formu Oluştur |
| Beslenen entity | Proje, Kalem |

**Toplantı referansı:** "Kırmızı yanıp sorulsun. Bir haftayı geçmiş, durumu askıda." (57:18), "44 bin liraya bu işi sana veririm dedi" (58:13)

---

#### E11 — Yönetim Dashboard (Paket 1 kapsamı — temel)

**Kullananlar:** YÖN (TV ekranına yansıtılacak)
**Amaç:** Satış hunisi ve genel durumu tek bakışta görmek.

| Bileşen | Detay |
|---------|-------|
| Satış hunisi | Gelen Teklif Talebi → Teklif Hazırlanıyor → Teklif Gönderildi → Cevap Bekliyor → Sipariş Onaylandı (her aşamadaki sayı + tutar) |
| Dikkat gerektiren | Cevapsız teklifler (1+ hafta), Muhasebe onay bekleyen, Termin yaklaşan |
| Dönem özeti | Bu ay/hafta: gelen talep, gönderilen teklif, onaylanan sipariş, iptal sayıları |
| Tip bazlı | Tip kodlarına göre (HS1K, HS4K...) dağılım |
| Yurtiçi/Yurtdışı | Oran ve tutar bazlı |
| Beslenen entity | Proje, Kalem, Firma |

**Toplantı referansı:** "Finalde üst yönetime TV'ye yansıtacağımız bir dashboard" (59:10), "Yukarıdaki büyük televizyonda gözükecek" (59:49)

---

### PAKET 2 — Satın Alma & Tedarik Zinciri

---

#### E12 — Satın Alma Talep Ekranı

**Kullananlar:** SA (görüntüler), TAS (talep oluşturur), ÜS (genel talep oluşturur)
**Amaç:** Satın almacının önüne düşen tüm taleplerin yönetimi.

| Bileşen | Detay |
|---------|-------|
| Talep listesi | Talep No, Talep Eden, Tarih, Proje No (varsa), Malzeme, Miktar, Öncelik, Durum |
| Filtreler | Talep tipi (proje/genel/sarf), Durum, Talep eden, Tarih |
| Talep detay | Malzeme detayı, madde kodu, ölçüler, bağlı proje bilgisi |
| Aksiyonlar | Kabul Et, Sipariş Oluştur, Reddet, Firma Seç |
| Beslenen entity | SatınAlmaTalebi, MalzemeKalemi, Kalem |

**Toplantı referansı:** "Tasarımcı girecek malzeme listesini. Satın almanın önüne düşecek talep olarak." (01:00:55), "Proje harici taleplerin de olabileceği bir satın alma ekranı" (01:09)

---

#### E13 — Satın Alma Sipariş Takibi

**Kullananlar:** SA, PM
**Amaç:** Dışarıya verilen siparişlerin takibi — hangi firmaya, ne zaman, geldi mi.

| Bileşen | Detay |
|---------|-------|
| Sipariş listesi | Sipariş No, Tedarikçi, Madde Kodu, Proje/Montaj No, Miktar, Fiyat, Sipariş Tarihi, Hedef Tarih, Durum |
| Renk kodları | Beklemede=beyaz, Yolda=mavi, Geldi=yeşil, Hedef aşıldı=kırmızı |
| Filtreler | Firma, Proje No, Malzeme grubu, Durum, Tarih |
| Toplu görünüm | Bir projenin TÜM malzemelerinin sipariş durumu (checklist gibi) |
| Aksiyonlar | Sipariş Oluştur, Geldi İşaretle (kısmi/tam), Fiyat Güncelle |
| Beslenen entity | SatınAlmaSiparişi, SatınAlmaTalebi, MalzemeKalemi |

**Toplantı referansı:** "Neleri sipariş vermiş, neler gelmiş, neler gelmemiş" (01:09), "Gelmemiş, kızarmış" (01:09)

---

#### E14 — Malzeme Durum Ekranı (Ofis Versiyonu)

**Kullananlar:** SA, PM, ÜS
**Amaç:** Bir projenin tüm malzemelerinin güncel durumu — sipariş verildi mi, geldi mi?

| Bileşen | Detay |
|---------|-------|
| Proje/montaj seçici | Proje No veya Montaj No ile sorgula |
| Malzeme tablosu | Malzeme, Grup, Adet, Sipariş Verildi mi, Tedarikçi, Sipariş Tarihi, Hedef Geliş, Geldi mi, Fiyat |
| Grup toplamları | İmalat: X/Y alındı, Keçe: X/Y alındı, Standart: X/Y alındı (progress bar) |
| Montaj hazırlık | Tüm malzemeler geldi mi? → Montaja hazır / Eksik var |
| Beslenen entity | SatınAlmaSiparişi, MalzemeKalemi, Kalem |

**Toplantı referansı:** "10 tane malzeme alınacakmış. 6 tanesi alınmış. %60'ı gelmiş." (01:55)

---

#### E15 — Malzeme Durum Ekranı (Atölye Versiyonu)

**Kullananlar:** OP, ÜS
**Amaç:** E14'ün basitleştirilmiş versiyonu — fiyat bilgisi YOK.

| Bileşen | Detay |
|---------|-------|
| Aynı yapı ama | Fiyat sütunları gizli, sipariş tarihi gizli |
| Ek bilgi | Beklenen geliş tarihi gösterilir |
| Sorgulama | Montaj no ile veya firma adı ile |
| Beslenen entity | SatınAlmaSiparişi, MalzemeKalemi (fiyat alanları hariç) |

**Toplantı referansı:** "Atölyede fiyatlar yok. Sadece gelme tarihini görüyor." (01:22)

---

#### E16 — Fason İş Takibi

**Kullananlar:** FAS, PM
**Amaç:** Dışarıya gönderilen işlerin durumu.

| Bileşen | Detay |
|---------|-------|
| Fason listesi | Montaj No, Parça, Fasoncu Firma, Gönderim Tarihi, Beklenen Dönüş, Durum |
| Renk | Fasonda=mavi, Gecikmiş=kırmızı, Döndü=yeşil |
| Aksiyonlar | Gönderildi İşaretle, Döndü İşaretle, Not Ekle |
| Beslenen entity | FasonİşTakibi, İşEmri |

**Toplantı referansı:** "Tedarik zinciri mühendisimiz var. Fason sürecini takip ediyor." (01:18)

---

#### E17 — Madde Kartı Yönetimi

**Kullananlar:** SA, MUH
**Amaç:** Madde kartlarını görüntüleme, ETA'dan senkronizasyon.

| Bileşen | Detay |
|---------|-------|
| Madde listesi | Madde Kodu, Tanım, Grup, Birim, Fiyat, Son Güncelleme |
| Filtreler | Grup (imalat/keçe/standart), arama |
| ETA Sync | "ETA'dan Çek" butonu — periyodik veya manuel |
| Eksik kontrolü | Programda kullanılan ama ETA'da olmayan kodları göster |
| Beslenen entity | MaddeKartı |

**Toplantı referansı:** "Madde kartlarından fiyat çekilebilir" (48:34), "Belirli periyotlarda çektirebiliriz" (01:38)

---

### PAKET 3 — Üretim & İstasyon Yönetimi

---

#### E18 — Proses Paket Yönetimi

**Kullananlar:** ÜS, TAS
**Amaç:** Standart iş emri şablonlarının tanımlanması ve yönetimi.

| Bileşen | Detay |
|---------|-------|
| Paket listesi | TKP1, TKP2... Paket Adı, Adım Sayısı, Kullanım Sayısı |
| Paket düzenleme | Sıralı adımlar: İstasyon, İşlem Adı, Tahmini Süre, Fason mı |
| Adım ekleme/çıkarma | Drag & drop sıralama |
| Aksiyonlar | Yeni Paket, Kopyala, Düzenle, Pasife Al |
| Beslenen entity | ProsesPaketi, ProsesAdımı |

**Toplantı referansı:** "TKP1, TKP2... Standart paketler seçilebilir" (01:19), "Tip 1'i seçecek, gelecek paket otomatik" (01:14)

---

#### E19 — İş Emri Oluşturma

**Kullananlar:** ÜS, TAS
**Amaç:** Bir kalemin malzemelerine proses paketleri atayarak iş emirlerini oluşturmak.

| Bileşen | Detay |
|---------|-------|
| Sol panel — Malzemeler | Kalemin imalat malzemeleri listesi |
| Sağ panel — Proses atama | Seçili malzeme için: TKP seç → adımlar otomatik gelir → düzenle (ekle/çıkar) → onayla |
| İş emri önizleme | Oluşacak tüm iş emirleri tablosu: Parça, Adım Sırası, İstasyon, Süre, Fason mı |
| Aksiyonlar | Paketten Oluştur, Manuel Adım Ekle, Onayla & Üretime Gönder |
| Beslenen entity | İşEmri, MalzemeKalemi, ProsesPaketi |

**Toplantı referansı:** "Büyük paketi çağırırım, bir adım çıkartırım, bir adım eklerim" (01:19)

---

#### E20 — İstasyon Ekranı (Tezgah Bazlı)

**Kullananlar:** OP
**Amaç:** Operatörün kendi tezgahında yapacağı işleri görmesi, barkod ile başlatıp bitirmesi.

| Bileşen | Detay |
|---------|-------|
| İstasyon seçimi | Login'de veya ekranda istasyon seç (CNC Torna 1, Freze 2 vb.) |
| İş listesi | Yapılabilir işler (yeşil) + devam eden (mavi) + bekleyen (sarı). Sıralı. |
| Her iş satırı | Montaj No, Parça Adı, İşlem, Adet (yapılan/kalan), Durum rengi |
| Barkod alanı | Teknik resimdeki barkodu oku → iş emrini bul |
| Aksiyonlar | BAŞLAT (barkod + tık), BİTİR (tık), kısmi tamamlama (X/Y adet) |
| FİYAT YOK | Operatör hiçbir fiyat bilgisi görmez |
| Beslenen entity | İşEmri, Kalem (fiyat alanları hariç) |

**Toplantı referansı:** "Sadece derin dermede neler yapacağım görmek istiyorum" (01:22), "Barkodu okusun, başladım desin, bitirdim desin" (01:24)

---

#### E21 — Üretim Durumu Matrisi

**Kullananlar:** ÜS, PM, YÖN
**Amaç:** Tüm projelerin tüm parçalarının hangi proses adımında olduğunu matrix görünümde görmek.

| Bileşen | Detay |
|---------|-------|
| Satırlar | Proje No + Montaj No + Parça Adı |
| Sütunlar | İstasyonlar: Testere → Torna → Freze → Delme → Taşlama → Kaplama → Kalite → Montaj → Sevk |
| Hücre | ✓ (tamamlandı/yeşil), ○ (yapılabilir/açık yeşil), ⏳ (devam ediyor/mavi), — (beklemede/gri), X (yok/boş) |
| Satın alma kolonu | Malzeme durumu: tamamı geldi ✓ / kısmen ○ / hiç gelmedi — |
| Filtreler | Proje, firma, istasyon, sadece aktif işler |
| Neden yapılmadı | Beklemedeki işe tıkla → neden bekliyor açıklaması |
| Beslenen entity | İşEmri, SatınAlmaSiparişi, Kalem |

**Toplantı referansı:** "CNC tornası yapılmış. Frezesi kalmış. Sonra kalite diye bitecek." (01:22), "Neden yapılmadığını görebilelim" (01:28)

---

#### E22 — Üretim Planlama (Gantt/Timeline)

**Kullananlar:** ÜS, PM
**Amaç:** İş emirlerinin zaman çizelgesinde gösterilmesi, planlama.

| Bileşen | Detay |
|---------|-------|
| Gantt görünüm | Satırlar: parçalar veya istasyonlar. Çubuklar: iş emirleri (süre bazlı) |
| Çakışma kontrolü | Aynı istasyonda aynı anda birden fazla iş varsa uyarı |
| Termin çizgisi | Proje termin tarihini dikey çizgi olarak göster |
| Beslenen entity | İşEmri, Kalem (termin), BoyutParametreleri (teorik süre) |

---

#### E23 — Gerçek Maliyet Analizi (Gelecek hazırlığı)

**Kullananlar:** YÖN
**Amaç:** Teklif fiyatı vs gerçek maliyet karşılaştırması.

| Bileşen | Detay |
|---------|-------|
| Proje seçimi | Tamamlanmış projeleri listele |
| Maliyet karşılaştırma | Teklif malzeme toplamı vs gerçek satın alma toplamı |
| Süre karşılaştırma | Teorik süre vs gerçek süre (başla/bitir) |
| Kâr/Zarar | Anlaşma fiyatı - (gerçek malzeme + gerçek işçilik) = kâr |
| Beslenen entity | FiyatlandırmaÇalışması, SatınAlmaSiparişi, İşEmri (süre), Kalem |

**Toplantı referansı:** "Gerçek maliyet... belki torna maliyeti iki katı. Satın alma standart diye üstünden durmadık ama karlı sandığımız iş aslında zarar" (01:35)

---

#### E24 — Gelişmiş Yönetim Dashboard (Paket 3 kapsamı)

**Kullananlar:** YÖN (TV ekranı)
**Amaç:** E11'in genişletilmiş versiyonu — üretim ve maliyet verileri dahil.

| Bileşen | Detay |
|---------|-------|
| E11'deki her şey + | |
| Üretim durumu | Aktif iş sayısı, biten iş sayısı, bekleyen, fason dışarıda |
| İstasyon doluluk | Her tezgahın şu an ne üzerinde çalıştığı |
| Maliyet trendi | Aylık: teklif toplamı vs gerçek maliyet toplamı → kâr trendi |
| Tip bazlı analiz | HS1K'dan yılda kaç adet, ortalama çarpan, ortalama kârlılık |
| Firma bazlı analiz | En çok iş yapılan firmalar, ciroları |
| Vade/tahsilat | Vadesi geçen, yaklaşan, açık bakiyeler |
| Beslenen entity | Tüm entity'ler |

**Toplantı referansı:** "Kaç silindir tiplerine göre kaç tane vermişim. Firma bazlı. Aylık bazlı." (01:55)

---

## 3. EKRAN SAYISI ÖZETİ

| Paket | Ekran | Sayı |
|-------|-------|------|
| **Paket 1** | E01-E11 | **11 ekran** |
| **Paket 2** | E12-E17 | **6 ekran** |
| **Paket 3** | E18-E24 | **7 ekran** |
| **Toplam** | | **24 ekran** |

---

## 4. ANA İŞ AKIŞLARI

### Akış 1: Teklif Talebi → Teklif Gönderimi

```
[Müşteriden talep gelir]
        │
        ▼
 PM: E01'de "Yeni Proje" ──► E02 açılır
        │                     Proje bilgilerini girer
        │                     Kalemleri tanımlar
        ▼
 PM: E02'de kalem seçer ──► E03 açılır
        │                    Boyut parametreleri girilir
        │                    "Malzeme Listesi Oluştur" tıklar
        ▼
 TAS: E04'te malzeme listesi oluşturur (UTA v1)
        │   Parçaları girer, temiz ölçüleri girer
        │   "Satın Almaya Gönder" tıklar
        ▼
 SA: E04'te (kendi görünümü) ham ölçüleri ve fiyatları girer
        │   Madde kartından otomatik çeker veya manuel girer
        │   "Kaydet" tıklar
        ▼
 PM: E05'te fiyatlandırma çalışması yapar
        │   3 yöntem hesaplanır, geçmiş projeler görülür
        │   Fiyat seçilir → kaleme yazılır
        ▼
 PM: E02'ye döner → tüm kalemler fiyatlandı
        │   Toplamları kontrol eder
        │   "PDF Oluştur" tıklar
        ▼
 PM: E06'da PDF oluşturur → mail gönderir
        │
        ▼
 E07'de "Teklif Gönderildi" otomatik tiklenir
 E10'da bekleyen teklifler listesine düşer
```

### Akış 2: Sipariş Onayı → Üretime Geçiş

```
[Müşteriden onay gelir]
        │
        ▼
 PM: E10'da sipariş onaylar
        │   Anlaşma fiyatı girilir (teklif fiyatından farklıysa)
        │   "Sipariş Onayla" tıklar
        ▼
 E03: Versiyon zincirinde otomatik yeni versiyon açılır
        │   Aşama: teklif → sipariş (asamadan_gecis)
        │   Son teklif versiyonu kilitlenir
        ▼
 TAS: E04'te sipariş malzeme listesini (USA) hazırlar
        │   Gerekirse nihai tasarıma göre revize eder
        │   "Satın Almaya Talep Gönder" tıklar
        ▼
 SA: E12'de talep düşer
        │   Malzemeleri inceler
        │   Firmalara sipariş geçer → E13'te takip eder
        ▼
 ÜS: E19'da iş emirlerini oluşturur
        │   Proses paketi seçer → adımları düzenler → onaylar
        ▼
 OP: E20'de işler görünür
        │   Barkod ile başlat/bitir
        │   İstasyon istasyon ilerler
        ▼
 ÜS/PM: E21'de matrix'ten takip eder
        │   Tüm parçalar + satın alma tamamlandığında
        ▼
 [Montaj → Kalite → Sevk → Fatura]
```

### Akış 3: Müşteri Değişiklik Talebi (Versiyon Açılması)

```
[Müşteri değişiklik ister — teklif veya sipariş aşamasında]
        │
        ▼
 PM: E03'te "Yeni Versiyon Aç" tıklar
        │   Değişiklik nedeni seçer (müşteri talebi)
        │   Açıklama yazar ("60mm → 110mm")
        ▼
 Mevcut aktif versiyon kilitlenir
 Yeni versiyon (v+1) açılır — öncekinin kopyası
        │
        ▼
 TAS: E04'te yeni versiyonda gerekli değişiklikleri yapar
        │
        ▼
 E03'te versiyon zincirinde tüm geçmiş görünür
        │   Diff butonu ile herhangi iki versiyon karşılaştırılabilir
        │
        ▼
 [Akış 1 veya 2'ye devam — aşamaya göre]
```

### Akış 4: Satın Alma Döngüsü

```
 [Talep düşer — E12]
        │
        ▼
 SA: Malzemeleri gruplandırır
        │   İmalat → Boru firma A, B'den teklif al
        │   Keçe → Standart firmadan sipariş geç
        │   Standart → Madde kartı fiyatıyla geç
        ▼
 SA: E13'te sipariş oluşturur
        │   Firma, miktar, fiyat, hedef tarih girer
        ▼
 [Malzeme gelince]
        │
 SA: E13'te "Geldi" işaretler
        │   E14/E15'te malzeme durumu güncellenir
        │   İlgili iş emrinin "malzeme mevcut" durumu aktif olur
        ▼
 OP: E20'de "yapılabilir" (yeşil) olarak görür
```

### Akış 5: Günlük Üretim Akışı (Operatör)

```
 OP: Sabah E20'yi açar (kendi istasyonu filtrelenmiş)
        │
        ▼
 Yapılabilir işler (yeşil) listesinde sıradaki işi seçer
        │
        ▼
 Teknik resimdeki barkodu okuttur
        │   → İş emri otomatik bulunur
        │   → "BAŞLAT" butonu aktif olur
        ▼
 "BAŞLAT" tıklar → zaman damgası başlar
        │   İş "devam ediyor" (mavi) olur
        ▼
 [İşi yapar]
        │
        ▼
 "BİTİR" tıklar → zaman damgası kapanır
        │   İş "tamamlandı" (yeşil) olur
        │   Bir sonraki istasyondaki iş "yapılabilir" olur
        ▼
 Sıradaki işe geçer
```

---

## 5. EKRANLARDAKİ PAYLAŞILAN BİLEŞENLER (Reusable Components)

| Bileşen | Kullanıldığı Ekranlar | Açıklama |
|---------|----------------------|----------|
| Proje/Kalem Seçici | E03, E05, E14, E15, E21, E23 | Proje no veya montaj no ile hızlı arama |
| Durum Badge | E01, E02, E10, E13, E16 | Renkli durum etiketi (enum → renk) |
| Malzeme Tablosu | E04, E14, E15 | Malzeme listesi grid'i (farklı sütun setleriyle) |
| Versiyon Timeline | E03 | Zincirdeki versiyonların kronolojik görünümü |
| Diff Görünümü | E03 | İki versiyon arasında eklenen/silinen/değişen satırlar |
| Progress Bar | E14, E21 | X/Y tamamlandı gösterimi |
| Barkod Okuyucu | E20 | Kamera veya el terminali ile barkod okuma |
| Filtre Bar | E01, E12, E13, E21 | Çoklu filtre + arama |
| Dashboard Kartı | E11, E24 | Sayı + trend (↑↓) + renk |
| PDF Önizleme | E06 | Embedded PDF viewer |

---

## 6. PLATFORM & TEKNİK NOTLAR

| Konu | Tercih/Not |
|------|------------|
| Erişim | Web tabanlı — ofis bilgisayarları + atölye bilgisayarları + TV ekranı |
| Responsive | Atölye ekranları büyük butonlu, touch-friendly olmalı (E20) |
| Barkod | Web kamera veya USB barkod okuyucu desteği |
| TV Dashboard | E11/E24 — fullscreen, auto-refresh, büyük font |
| Çevrimdışı | Gerekli değil — tüm cihazlar ağda |
| ETA Bağlantısı | SQL Server üzerinden, periyodik sync (canlı değil) |
| Concurrent users | ~15-20 aynı anda (küçük-orta ölçek) |

---

*Bu envanter, veri modeli (univers-veri-modeli.md) ile birebir uyumlu olarak oluşturulmuştur. Her ekranın besleneceği entity'ler belirtilmiştir.*
