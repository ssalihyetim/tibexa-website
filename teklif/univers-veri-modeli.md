# Ünverler Makine ERP — Entity-Relationship Veri Modeli
## Toplantı Transkriptinden Çıkarılan Kapsamlı Analiz

> Kaynak: UniversMeetingTscrip.md (04.05.2026)
> Hazırlayan: Tibexa

---

## 1. ENTITY KATALOĞU

### 1.1 Firma (Customer / Müşteri)

Ünverler Makine'nin teklif verdiği ve sipariş aldığı firmalar.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | Sistem ID | "Sen kendin programında bir ID versin" (41:30) |
| musteri_kodu | string | | ETA müşteri kodu | "Müşteri kodu yokmuş" (13:22) — bazen boş olabiliyor |
| firma_adi | string | ✓ | Firma adı | "Hangi firma?" (07:37) |
| ulke | enum | ✓ | Yurtiçi/Yurtdışı | "Ne kadarı yurt dışı?" (01:55) |
| odeme_kosullari | string | | Varsayılan ödeme koşulları | "Ödeme koşulları neymiş?" (07:37) |
| para_birimi | enum | | EUR/TRY/USD | "Euro muymuş?" (07:37) |
| notlar | text | | Firmaya özel notlar | "Bunun ödemesi peşin alınacak" (46:58) |
| eta_firma_kodu | string | | ETA'daki firma kodu | ETA entegrasyonu için |
| created_at | timestamp | ✓ | | |
| updated_at | timestamp | ✓ | | |

**İş Kuralları:**
- Bir firmanın N adet projesi olabilir
- Firma bazlı analiz yapılabilmeli (firma bazlı kaç teklif, kaç sipariş, toplam ciro)

---

### 1.2 Proje (Talep)

Ana talep kaydı. Müşteriden gelen her teklif talebi bir proje.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | Sistem ID | |
| proje_no | string/unique | ✓ | "P-112" formatı, artan | "Talep numarası, P. Örnekle 112" (00:09) |
| firma_id | FK→Firma | ✓ | Müşteri | |
| talep_tarihi | date | ✓ | Talebin geldiği tarih | "Hangi tarihte yapılmış?" (07:37) |
| odeme_kosullari | string | | Bu projeye özel vade | "Ödeme koşulları neymiş?" (07:37) |
| para_birimi | enum | ✓ | EUR/TRY/USD | "Euro muymuş?" (07:37) |
| paket_adet | decimal | | Paket adedi | "Paket aradı kaçmış?" (07:37) |
| toplam_teklif_tutari | decimal | | Teklifin toplam tutarı | "Toplam teklif tutarı neymiş?" (07:37) |
| durum | enum | ✓ | acik/beklemede/onaylandi/iptal | "Bu teklif açıldı mı, beklemede mi, iptal mi oldu?" (07:37) |
| onay_tarihi | date | | Sipariş onay tarihi | "Onaylandıysa hangi tarihte onaylandı?" (07:37) |
| iptal_tarihi | date | | İptal tarihi | "İptal olduysa hangi tarihte" (07:37) |
| iptal_nedeni | text | | Neden iptal oldu | "Hangi nedenden iptal oldu?" (07:37) |
| dil | enum | ✓ | TR/EN/DE | "Dili Türkçeden İngilizceye çevirdiğimiz zaman" (09:59) |
| form_tipi | enum | ✓ | teklif/proforma/siparis_onay | "Teklif olacak, pro forma olacak, ordür olacak" (10:53) |
| teslim_suresi | string | | Teslimat süresi bilgisi | "Testin tarihi neymiş?" (07:37) |
| gumruk_islemleri | text | | Gümrük bilgileri | "Gümrük işlemleri var" (05:07) |
| iskonto | decimal | | İskonto oranı/tutarı | "İskonto gibi kalemler var" (05:07) |
| kdv_orani | decimal | | KDV oranı | "KDV var" (05:07) |
| muhasebe_onay | boolean | ✗ | Muhasebe kontrolü yapıldı mı | "Muhasebe belki okey vermeden üretime başlanmaması" (01:55) |
| notlar | text | | Proje notları | "Manuel açıklama kısmı da olur" (46:58) |
| created_at | timestamp | ✓ | | |
| updated_at | timestamp | ✓ | | |

**İş Kuralları:**
- Proje numarası otomatik artan, benzersiz
- Bir projenin altında N adet kalem olabilir
- "Bazen 10 kalem oluyor. Bazen 5 kaleme biz teklif veriyoruz ama bunların içinden sadece 2 tanesi onaylanıyor." (03:50)
- Muhasebe onayı olmadan satın alma/üretim başlatılamaz (uyarıyla esnetilebilir)
- Durum "beklemede" ise ve 1 hafta geçtiyse → kırmızı uyarı (07:37, 57:18)
- İptal olduğunda neden zorunlu

---

### 1.3 Kalem (Proje Kalemi / Teklif Kalemi)

Proje altındaki her bir ürün/montaj birimi. Ünverler Makine'nin temel iş birimi.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | Sistem ID | |
| proje_id | FK→Proje | ✓ | Hangi projeye ait | |
| kalem_no | string | ✓ | "P112-1", "P112-2" formatı | "Kalemleri tire 1, tire 2'den 21'e kadar" (05:10) |
| montaj_no | string | ✓ | Montaj numarası — TÜM SİSTEMİN OMURGASI | "Tüm üretim, tüm satın alma... bu montaj numarasının üzerinden yürüyor" (40:21) |
| urun_tanimi | string | ✓ | "135-1275 Rupi Atlas Silindir İmalatı" | (00:09) |
| tip_kodu | enum | | HS1K, HS4K vb. silindir tip kodu | "Bu silindirin hangi tip olduğu... 15 tane" (19:49) |
| proses_kodu | string | | Hangi proses grubuna ait | "Hidrolik silindir prosesi" (46:58) |
| adet | integer | ✓ | Sipariş adedi | "Birer adetmiş" (13:22) |
| sevk_edilen_adet | integer | | Sevk edilen | "Birer tanesini göndermişiz" (13:22) |
| kalan_adet | computed | | adet - sevk_edilen_adet | |
| birim_fiyat | decimal | | Birim fiyatı (teklif) | "Birim fiyatları" (13:22) |
| toplam_fiyat | decimal | | birim_fiyat × adet | "Toplam fiyatlar" (13:22) |
| anlasma_fiyati | decimal | | Müşteriyle anlaşılan nihai fiyat | "Teklif edilen fiyat, anlaşma fiyatı" (58:13) |
| secilen_carpan | decimal | | Kullanılan fiyat çarpanı | "Ben bunu 2 ile çarpıp müşteriye göndereceğim" (55:23) |
| fiyat_yontemi | enum | | carpan/hacim/sure/manuel | 3 farklı fiyatlandırma yöntemi (43:47) |
| siparis_tarihi | date | | Sipariş onay tarihi | "Sipariş tarihi buymuş" (13:22) |
| termin_tarihi | date | | Termin tarihi | "Termin tarihi buymuş" (13:22) |
| termin_haftasi | integer | | Termin haftası | "Termin haftası buymuş" (13:22) |
| sevk_tarihi | date | | Fiili sevk tarihi | "Biz 26.06'da da sevk etmişiz" (13:22) |
| durum | enum | ✓ | teklif/siparis/uretimde/sevk/fatura/iptal | "Durumu teklif mi, sipariş mi, onaylandı mı, iptal mi?" (19:51) |
| ilave_aciklama | text | | Ek açıklama | "İlave açıklama varsa" (13:22) |
| created_at | timestamp | ✓ | | |
| updated_at | timestamp | ✓ | | |

**İş Kuralları:**
- Montaj numarası TÜM SİSTEMİN ANAHTARI — satın alma, üretim, fason, maliyet her şey bunun üzerinden yürüyor
- Kısmi sevkiyat yapılabilir: "Bir takımını şimdi keselim, bir takımını sonra keselim de oluyor" (06:46)
- Kısmi faturalama: "Sadece o kalemin faturasını kes diyoruz" (06:25)
- Kalem bazında bağımsız yaşam döngüsü
- Her kalemin ayrı termin tarihi olabilir: "20. haftada istiyor, bazılarını 26. haftada" (05:44)

---

### 1.4 Boyut Parametreleri (Kalem Ölçüleri)

Her kalemin temiz (bitmiş) ve ham (satın alınacak) ölçüleri. Formülizasyonun temeli.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| kalem_id | FK→Kalem | ✓ | | |
| temiz_dis_cap | decimal | | Bitmiş ürün dış çapı | "X, Y, Z... dış çap, iç çap, boy" (25:55) |
| temiz_ic_cap | decimal | | Bitmiş ürün iç çapı | |
| temiz_boy | decimal | | Bitmiş ürün boyu | |
| ham_dis_cap | decimal | | Ham malzeme dış çapı | "Hem temiz ölçüde hem satın almanın yazacağı fail ölçüde" (27:09) |
| ham_ic_cap | decimal | | Ham malzeme iç çapı | |
| ham_boy | decimal | | Ham malzeme boyu | |
| hesaplanan_hacim | computed | | Formüllerle hesaplanan | "Bunun hacmi bu kadar diyeceğiz" (26:26) |
| hesaplanan_talas | computed | | Kaldırılacak talaş miktarı | "Şu kadar metreküp talaş kaldıracakmışız" (26:26) |
| teorik_sure | computed | | Formüllerle hesaplanan işleme süresi | "Zaten bunun işleme süresi bu diyecek" (25:06) |

**İş Kuralları:**
- "6 kutucuğun birbiriyle formülize edilebiliyor olması" (27:09)
- Temiz ölçüyü tasarımcı girer, ham ölçüyü satın almacı girer
- Bu 6 alan + admin formülleri = tüm fiyatlandırma ve planlama hesapları

---

### 1.5 Admin Formülleri

Yönetici tarafından tanımlanan ve değiştirilebilen hesaplama formülleri.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| formul_adi | string | ✓ | "Hacim hesaplama", "Talaş süresi" | |
| formul_ifadesi | string | ✓ | Matematiksel ifade | "Hacim hesaplama şu formunda olacak" (28:10) |
| carpan_degeri | decimal | | Sabit çarpan | "Bunu 1.58 ile çarp" (29:15) |
| aciklama | text | | Formülün ne yaptığı | |
| tip_kodu | string | | Hangi tip için geçerli (null = hepsi) | |
| aktif | boolean | ✓ | | |

**İş Kuralları:**
- "Admin ekranı gibi. Ben diyeceğim ki hacim hesaplama şu formunda olacak" (28:10)
- "Bunu işte atıyorum yandaki tabloda buna bir üç diyeceğiz. Üçte çarpacak" (28:10)
- Formüller boyut parametrelerini (temiz/ham ölçüler) referans alabilmeli
- Yönetici istediği zaman değiştirebilmeli

---

### 1.6 Malzeme Listesi (BOM — Bill of Materials)

Bir kalemin tüm yaşam döngüsü boyunca geçtiği malzeme çalışmaları. UTA (teklif) ve USA (sipariş) ayrı entity değil, aynı zincirin farklı aşamalarıdır. Her versiyon bir öncekinin üzerine oluşur ve tüm geçmiş görülebilir.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| kalem_id | FK→Kalem | ✓ | Hangi kaleme ait | |
| asama | enum | ✓ | teklif / siparis | "UTA çalışması... USA çalışması" (31:53) |
| versiyon | integer | ✓ | Sıralı versiyon: v1, v2, v3... | "Revizyon 1, revizyon 2 gibi tutulması gerekiyor" (32:36) |
| parent_id | FK→self | | Bir önceki versiyon (null = ilk versiyon) | "İlk halini bulmalı" (36:29) |
| degisiklik_nedeni | enum | | musteri_talebi / tasarim_revizyonu / fiyat_degisikligi / asamadan_gecis | Neden yeni versiyon açıldı |
| degisiklik_aciklamasi | text | | Serbest metin: ne değişti | "Müşterimin isteği değişti. 60mm değil 110mm" (33:23) |
| durum | enum | ✓ | taslak / aktif / kilitli | "Siparişe döndü ya, kilitlenecek" (35:12) |
| olusturan | FK→User | ✓ | Kim oluşturdu | |
| onaylayan | FK→User | | | |
| created_at | timestamp | ✓ | | |
| kilitlenme_tarihi | timestamp | | Versiyon kilitlendiğinde | |

**Versiyon Zinciri Örneği:**
```
Kalem P112-1 için:

v1  [teklif]   taslak    → İlk UTA çalışması, tasarımcı oluşturdu
v2  [teklif]   aktif     → Müşteri 60mm→110mm istedi, tasarımcı revize etti
v3  [teklif]   kilitli   → Teklif gönderildi, bu versiyon kilitlendi
v4  [siparis]  aktif     → Sipariş onaylandı, v3'ün kopyasından USA oluştu
v5  [siparis]  kilitli   → Nihai tasarım yapıldı, küçük revizyon, kilitlendi (final)
```

**İş Kuralları:**
- UTA ve USA aynı tabloda, `asama` alanıyla ayrılır. Böylece tek bir zincirde tüm geçmiş görülür.
- Her versiyon bir öncekiyle `parent_id` ile bağlıdır → baştan sona izlenebilirlik.
- Bir versiyon `aktif` durumdayken editlenebilir. `kilitli` olunca dokunulmaz.
- Yeni değişiklik gerektiğinde: mevcut aktif/kilitli versiyonun kopyası alınır → yeni versiyon açılır.
- Aşama geçişi (teklif→sipariş) de bir versiyon oluşturur: `degisiklik_nedeni = asamadan_gecis`
- "İki ayrı liste olacak. İki aradaki farkı da görebilelim" (34:11) — herhangi iki versiyon diff'lenebilir.
- "Teklif aşamasında da malzemesi değişiyor, editlenebilir" (34:03) — teklif aşamasında da N versiyon olabilir.
- "Finaller birbiriyle örtüşmesi lazım. Çünkü teklifle gelmeye çalışmışız. Belki arada malzeme fiyatı arttı. Gerçekten kâr mı etmişiz?" (36:30) — teklif finali vs sipariş finali karşılaştırılabilir.

---

### 1.7 Malzeme Kalemi (BOM Satırı)

Malzeme listesindeki her bir satır.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| malzeme_listesi_id | FK→MalzemeListesi | ✓ | | |
| sira_no | integer | ✓ | Liste sırası | |
| malzeme_grubu | enum | ✓ | imalat/kece/standart/sarf | "İmalat malzemeleri, keçe, standart" (02:48) |
| madde_kodu | string | | ETA madde kodu | "Madde kodunun da zaten fiyatı belli" (24:15) |
| tanim | string | ✓ | Malzeme tanımı | "Bir tane boru, bir tane kapak" (21:59) |
| adet | decimal | ✓ | Gereken adet | "Bu kadar lazım diyor" (21:59) |
| birim | string | | Adet/kg/metre | |
| temiz_dis_cap | decimal | | Temiz ölçü (tasarımcı girer) | "Tasarım temiz ölçüleri oluşturuyor" (24:15) |
| temiz_ic_cap | decimal | | | |
| temiz_boy | decimal | | | |
| ham_dis_cap | decimal | | Ham ölçü (satın almacı girer) | "Satın alma adet sonrasındaki alınacak malzemelerin ölçülerini yazıyor" (24:15) |
| ham_ic_cap | decimal | | | |
| ham_boy | decimal | | | |
| birim_fiyat | decimal | | Malzeme birim fiyatı | "Kilogram fiyatları belli" (24:15) |
| toplam_fiyat | decimal | | birim_fiyat × adet × kg_hesap | |
| fiyat_kaynagi | enum | | madde_karti/manuel/son_alis | "Madde kartındaki fiyatı getir / En son fiyatı getir" (44:51) |

**İş Kuralları:**
- Tasarımcı ürünün parçalarını ve temiz ölçülerini girer, satın almaya gönderir
- Satın alma ham ölçülerini ve fiyatlarını girer
- Standart/keçe grubu fiyatları madde kartından otomatik çekilebilir
- İmalat grubu: Hacim × kg fiyatı ile otomatik hesap mümkün (%40'ı standart madde kartı var)
- "Satın alma hepsini manuel giriyor. Ama bunların madde kartları var" (48:34)

---

### 1.8 Madde Kartı

ETA'dan çekilen veya manuel girilen malzeme referans bilgileri.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| madde_kodu | string/unique | ✓ | ETA madde kodu | "Tüm madde kodları mevcut" (44:51) |
| tanim | string | ✓ | Malzeme açıklaması | |
| malzeme_grubu | enum | ✓ | imalat/kece/standart | "Keçe grubu, standart grup, imalat grubu" (24:15) |
| birim | string | ✓ | kg/adet/metre | |
| birim_fiyat | decimal | | Güncel fiyat | |
| fiyat_guncelleme_tarihi | date | | Son güncelleme | |
| kg_fiyat | decimal | | Kilogram başına fiyat (imalat malzeme) | "Kilogram fiyatları belli" (24:15) |
| eta_sync_tarihi | timestamp | | ETA'dan en son ne zaman çekildi | |
| aktif | boolean | ✓ | | |

**İş Kuralları:**
- "Standart grubun fiyatları altı ayda bir güncelleniyor" (satır ~476)
- ETA'dan periyodik çekilir, canlı entegrasyon gerekmez
- "Bir kere çekmemiz yeterlidir. Sürekli olarak çekmeye gerek yok. Belirli periyotlarda çektirebiliriz" (01:38)
- Yeni madde kartı gerektiğinde "muhasebeye söylüyoruz, ETA'da açıyorlar" (01:38)

---

### 1.9 Fiyatlandırma Çalışması

Bir kalem için yapılan fiyat hesaplama ve karar kaydı.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| kalem_id | FK→Kalem | ✓ | | |
| toplam_malzeme_fiyati | decimal | | Malzeme listesinden gelen toplam | "Toplam malzeme fiyatı bu kadarmış" (42:20) |
| imalat_malzeme_toplam | decimal | | İmalat malzemeleri alt toplamı | "İmalat malzemelerimizin toplam fiyatı bu kadarmış" (42:20) |
| kece_toplam | decimal | | Keçeler alt toplamı | "Keçeler buymuş" (01:55) |
| standart_toplam | decimal | | Standart malzeme alt toplamı | "Standart malzemeleri buymuş" (01:55) |
| carpan_bazli_fiyat | decimal | | Malzeme × çarpan | "Malzeme fiyatını ikiyle çarp" (43:47) |
| secilen_carpan | decimal | | Kullanılan çarpan | |
| hacim_bazli_fiyat | decimal | | Hacim hesabından gelen fiyat | "Toplam hacmine göre şu çıkıyor" (44:36) |
| sure_bazli_fiyat | decimal | | Teorik süre × gün fiyatı | "İşleme süresi × 2000 lira" (53:04) |
| secilen_fiyat | decimal | | Finalde seçilen fiyat | "Birini seçeceğim" (53:29) |
| secilen_yontem | enum | | carpan/hacim/sure/manuel | |
| created_by | FK→User | ✓ | | |
| created_at | timestamp | ✓ | | |

**İş Kuralları:**
- 3 farklı fiyatlandırma yöntemi hesaplanıp yan yana gösterilir
- Geçmiş benzer projeler de aynı ekranda görülür (tip kodu bazlı filtreleme)
- "Bana böyle 3 tane fiyat getirecek. Bir de eski fiyat teklifleri göreceğim. Oradan karar vereceğim." (53:04)
- Karar veren kişi proje müdürü veya yönetim (rol bazlı erişim)

---

### 1.10 Satın Alma Talebi

Tasarım veya üretimden satın almaya düşen talep.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| kalem_id | FK→Kalem | | Proje kalemiyle ilişki (varsa) | |
| talep_eden | FK→User | ✓ | Kim talep etti | "Tasarımcı girecek... Satın almanın önüne düşecek" (01:00:55) |
| talep_tipi | enum | ✓ | proje/genel/sarf | "Proje harici taleplerin de olabileceği" (01:09) |
| malzeme_kalemi_id | FK→MalzemeKalemi | | Malzeme listesi satırıyla ilişki | |
| aciklama | text | | Serbest metin açıklama | "Bana şu elmas kalsın" (01:35) |
| miktar | decimal | ✓ | | |
| oncelik | enum | | normal/acil | |
| durum | enum | ✓ | beklemede/onaylandi/siparis_verildi/tamamlandi | |
| created_at | timestamp | ✓ | | |

**İş Kuralları:**
- Tasarımcı USA'yı tamamladığında otomatik olarak satın alma talepleri oluşur
- Üretim de genel talep girebilir (elmas, sarf malzeme vb.)
- "Sadece tasarımcı girmeyecek belki üretimin de girebileceği... sarf malzemelerin de talep edilebileceği" (01:09)

---

### 1.11 Satın Alma Siparişi

Satın almacının dışarıya verdiği siparişler.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| talep_id | FK→SatınAlmaTalebi | | İlişkili talep | |
| tedarikci_firma | string | ✓ | Sipariş verilen firma | "3-4 tane firma var" (01:09) |
| madde_kodu | string | | | |
| kalem_id | FK→Kalem | | Montaj numarası ile ilişki | "Gene montaj numaraları aynı" (01:09) |
| miktar | decimal | ✓ | Sipariş miktarı | |
| birim_fiyat | decimal | | | |
| toplam_fiyat | decimal | | | |
| siparis_tarihi | date | ✓ | | |
| hedef_teslim_tarihi | date | | Beklenen geliş tarihi | "Hedef tarihi neymiş gelmesi için" (01:09) |
| gercek_teslim_tarihi | date | | Gerçek geliş tarihi | |
| durum | enum | ✓ | siparis_verildi/yolda/geldi/eksik | |

**İş Kuralları:**
- Hedef tarihi geçen siparişler kırmızıya döner: "Gelmemiş, kızarmış" (01:09)
- Aynı talep birden fazla firmaya kırılabilir
- "Hangisinin elinde varsa, hangisinin fiyatı uygunsa" (01:09)

---

### 1.12 Proses Paketi (TKP — İş Emri Şablonu)

Standart üretim proses paketleri.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| paket_kodu | string/unique | ✓ | TKP1, TKP2, TKP3... | "TKP1, TKP2, TKP3" (01:19) |
| paket_adi | string | ✓ | "Upcount Gövde Proses 1" | |
| aciklama | text | | | |
| aktif | boolean | ✓ | | |

---

### 1.13 Proses Adımı (TKP Satırı)

Bir proses paketinin içindeki sıralı iş adımları.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| paket_id | FK→ProsesPaketi | ✓ | | |
| sira_no | integer | ✓ | İşlem sırası | |
| istasyon | enum | ✓ | torna/freze/taslama/kaplama/kalite/montaj/sevkiyat/fason | "Freze, CNC, torna, taşlama, kaplama, kalite, sevkiyat" (01:14) |
| islem_adi | string | ✓ | İşlem tanımı | |
| tahmini_sure | interval | | Teorik süre | |
| fason_mi | boolean | | Dışarıya mı çıkacak | "Bu fasona dışarı çıkacak" (01:18) |

**İş Kuralları:**
- "Standart bir şey çağrılıp belki bir kalem daha tezgahta eklenebilir" (01:14)
- Paket seçilir, gerekirse adım eklenir/çıkarılır
- "Adam tip 1'i seçecek, gelecek paket otomatik. Ya kabul edecek, ya tip 2'yi seçecek" (01:14)

---

### 1.14 İş Emri

Bir kalemin bir malzemesinin bir proses adımı = 1 iş emri.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | Sistem ID | |
| kalem_id | FK→Kalem | ✓ | Montaj numarası üzerinden | |
| malzeme_kalemi_id | FK→MalzemeKalemi | ✓ | Hangi parça | |
| proses_adimi_id | FK→ProsesAdımı | | Şablondan geldiyse | |
| sira_no | integer | ✓ | Proses sırası | |
| istasyon | enum | ✓ | Hangi tezgah/istasyon | |
| islem_adi | string | ✓ | | |
| planlanan_adet | integer | ✓ | Kaç adet yapılacak | |
| tamamlanan_adet | integer | | Kaç adet bitti | "Bundan 4 tane yapılacakmış. 2'sini yapmışım" (01:27) |
| durum | enum | ✓ | beklemede/yapilabilir/devam_ediyor/tamamlandi | |
| onceki_is_emri_id | FK→self | | Bağımlılık — önceki adım | |
| fason_mi | boolean | | Dışarıya mı çıkıyor | |
| baslama_zamani | timestamp | | Barkod ile başlatma | "Barkodu okusun, başladım desin" (01:24) |
| bitis_zamani | timestamp | | Barkod ile bitirme | "Bitir deyince bitirecek" (01:32) |
| gercek_sure | interval | computed | bitiş - başlangıç | |
| teorik_sure | interval | | Formülden gelen süre | |
| operator_id | FK→User | | Kim yaptı | "Kullanıcı girişini yaptıktan sonra" (01:32) |
| neden_yapilmadi | text | | Beklemedeyse neden | "Neden yapılmadığını görebilelim" (01:28) |

**İş Kuralları:**
- Durum mantığı:
  - **beklemede**: Önceki iş emri bitmedi VEYA malzeme gelmedi → sarı/gri
  - **yapilabilir**: Önceki adım tamam VE malzeme mevcut → yeşil
  - **devam_ediyor**: Barkod ile başlatıldı → mavi
  - **tamamlandi**: Barkod ile bitirildi → koyu yeşil
- "Senin bir önceki istasyonunda bu iş bitmiş. Malzeme gelmiş. Yeşil gösteriyor." (01:26)
- "Bir önceki iş emri hazır değil. Yetire gösteriyor." (01:26)
- Kısmi tamamlama: 4 adetten 2'si yapıldı, 2 kaldı
- Tezgah/istasyon bazlı filtreleme: "Sadece derin dermede neler yapacağım onları görmek istiyorum" (01:22)
- İleride gerçek süre vs teorik süre karşılaştırması yapılacak
- İleride duruş kodları eklenebilecek (setup, elmas değişimi vb.)

---

### 1.15 Fason İş Takibi

Dışarıya gönderilen işlerin takibi.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| is_emri_id | FK→İşEmri | ✓ | İlgili iş emri | |
| fason_firma | string | ✓ | Fasoncu firma | |
| gonderim_tarihi | date | | Ne zaman gönderildi | |
| beklenen_donus_tarihi | date | | | |
| gercek_donus_tarihi | date | | | |
| durum | enum | ✓ | gonderildi/fasonda/dondu | |
| notlar | text | | | |

**İş Kuralları:**
- "Tedarik zinciri mühendisimiz var. O da fason sürecini takip ediyor." (01:18)
- Fason iş emrinden otomatik oluşur
- Dönüş olduğunda bir sonraki proses adımı aktif olur

---

### 1.16 Proje Takip Adımları (Workflow)

Her projenin geçtiği aşamaların takibi — otomatik tarih damgalı.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| kalem_id | FK→Kalem | ✓ | | |
| adim | enum | ✓ | tasarim_basladi/tasarim_bitti/satin_alma_fiyat_girdi/teklif_hazirlandi/teklif_gonderildi/siparis_onaylandi/usa_basladi/usa_bitti/satin_alma_talep/uretim_basladi/montaj/kalite/sevk/fatura | |
| tamamlandi | boolean | ✓ | Tick atıldı mı | "Tikleniyor. Tarih sağ girmiş olacak." (46:08) |
| tamamlanma_tarihi | timestamp | | Otomatik — tick atıldığında | "Tiklenecek zaman tarih otomatik gelecek" (45:37) |
| tamamlayan | FK→User | | Kim tikledi | |

**İş Kuralları:**
- "Satın alma fiyatları girip bir onay tik atsa, benim çalışmam bitti diye zaten buraya tarih gelecek" (45:37)
- Dashboard bu adımlardan beslenir
- Her kalem bağımsız ilerleme gösterir

---

### 1.17 Kullanıcı ve Roller

| Alan | Tip | Zorunlu | Açıklama |
|------|-----|---------|----------|
| id | UUID/PK | ✓ | |
| ad_soyad | string | ✓ | |
| email | string | ✓ | |
| rol | enum[] | ✓ | yonetim/proje_muduru/satisci/tasarimci/satin_almaci/uretim_sorumlu/operator/muhasebe |
| aktif | boolean | ✓ | |
| varsayilan_istasyon | string | | Operatör için varsayılan tezgah |

**İş Kuralları:**
- Rol bazlı erişim: "Belki bu detayların hepsini görmesini istemeyebiliriz" (54:04)
- Operatör: Fiyat görmez, sadece iş emri ve malzeme durumu
- Satışçı: Teklif formu ve fiyat ekranı
- Yönetim: Her şeyi görür + dashboard
- Tasarımcı: Malzeme listesi + ölçü girişi
- Satın almacı: Fiyat girişi + sipariş takibi + malzeme durumu

---

### 1.18 PDF Şablonu

Sistem tarafından üretilen belge tipleri.

| Alan | Tip | Zorunlu | Açıklama | Toplantı Referansı |
|------|-----|---------|----------|-------------------|
| id | UUID/PK | ✓ | | |
| sablon_adi | string | ✓ | "Teklif TR", "Sipariş Onay EN" | |
| form_tipi | enum | ✓ | teklif/proforma/siparis_onay | "Teklif, pro forma, ordür, sipariş" (10:53) |
| dil | enum | ✓ | TR/EN/DE | "İngilizcesi, Türkçesi, Almancası" (09:59) |
| isimlendirme_formati | string | ✓ | "{proje_no}-{firma}-{tarih}-{tip}" | "Sipariş numarası-müşteri-tarih" (10:49) |
| aktif | boolean | ✓ | | |

**İş Kuralları:**
- Şu an 4-5 kombinasyon var, dil eklendikçe artabilir
- PDF otomatik oluşturulup havuza kaydedilir
- Mail gönderiminde havuzdan çekilir

---

## 2. İLİŞKİ DİYAGRAMI (Metin Formatı)

```
Firma (1) ──────────────── (N) Proje
                                 │
                                 │ 1:N
                                 ▼
                              Kalem ◄─────── BoyutParametreleri (1:1)
                                │
                   ┌────────────┼────────────────────┐
                   │            │                     │
                   ▼            ▼                     ▼
           MalzemeListesi   FiyatlandirmaCal.    ProjeTakipAdimlari
           (UTA/USA)            │                (workflow ticks)
              │                 │
              │ 1:N             │
              ▼                 │
         MalzemeKalemi ◄────────┘
              │         (fiyat hesabı buradan)
              │
         ┌────┴─────┐
         ▼           ▼
   SatinAlmaTalebi  İşEmri
         │            │
         ▼            │
   SatinAlmaSiparisi  ├──────► FasonIsTakibi
                      │
                      │ (barkod başla/bitir)
                      ▼
                   Operatör Ekranı


ProsesPaketi (1) ── (N) ProsesAdimi
       │
       └──── İşEmri oluşturulurken şablon olarak kullanılır


MaddeKarti ◄──── ETA Sync (periyodik)
    │
    └──── MalzemeKalemi.madde_kodu ile eşleşir


Kullanici ──── Roller ile erişim kontrolü
    │
    └──── Her işlemde kim yaptı / kim gördü


PDF Sablonu ──── Proje.form_tipi + Proje.dil ile eşleşir
```

---

## 3. ENUM DEĞERLERİ

### proje_durum
`acik` → `teklif_gonderildi` → `beklemede` → `onaylandi` | `iptal`

### kalem_durum
`teklif` → `siparis` → `uretimde` → `montajda` → `kalitede` → `sevk_edildi` → `faturalandi`

### malzeme_grubu
`imalat` | `kece` | `standart` | `sarf`

### malzeme_listesi_asama
`teklif` (UTA — teklif çalışması) | `siparis` (USA — sipariş çalışması)

### malzeme_listesi_degisiklik_nedeni
`musteri_talebi` | `tasarim_revizyonu` | `fiyat_degisikligi` | `asamadan_gecis`

### is_emri_durum
`beklemede` (sarı) → `yapilabilir` (yeşil) → `devam_ediyor` (mavi) → `tamamlandi` (koyu yeşil)

### istasyon
`cnc_torna` | `universal_torna` | `freze` | `derin_delme` | `taslama` | `kaplama` | `kaynak` | `testere_kesim` | `radyal_matkap` | `kalite` | `montaj` | `sevkiyat` | `fason`

### kullanici_rol
`yonetim` | `proje_muduru` | `satisci` | `tasarimci` | `satin_almaci` | `uretim_sorumlu` | `operator` | `muhasebe` | `fason_takip`

### para_birimi
`TRY` | `EUR` | `USD`

### dil
`TR` | `EN` | `DE`

### form_tipi
`teklif` | `proforma` | `siparis_onay` | `fatura`

### fiyat_yontemi
`carpan` | `hacim` | `sure` | `manuel`

### satin_alma_talep_tipi
`proje` | `genel` | `sarf`

---

## 4. KRİTİK İŞ KURALLARI ÖZETİ

### 4.1 Montaj Numarası = Sistem Omurgası
> "Bizim tüm üretim, tüm satın alma, tüm veri ilişkileri bu montaj numarasının üzerinden yürüyor." (40:21)

Her entity montaj numarası (kalem_id) üzerinden ilişkilendirilir. Bu, raporlama ve izlenebilirliğin temelidir.

### 4.2 Kesintisiz Versiyon Zinciri (UTA ↔ USA)
> "Üzerinde editlenebilir değil. Yeni oluşturulacak. İki ayrı şey olacak." (34:11)

UTA ve USA aynı tabloda, tek bir versiyon zincirinde yaşar. Kurallar:

1. **Aktif versiyon editlenebilir.** Değişiklik kaydedildiğinde (müşteri talebi, tasarım revizyonu vb.) mevcut versiyon kilitlenir, yeni versiyon (v+1) açılır.
2. **Aşama geçişi de bir versiyondur.** Teklif→sipariş geçişinde son teklif versiyonu kilitlenir, yeni bir sipariş versiyonu açılır (`degisiklik_nedeni = asamadan_gecis`).
3. **Hiçbir zaman overwrite yapılmaz.** Her değişiklik yeni kayıt, parent_id ile öncekine bağlı.
4. **Herhangi iki versiyon diff'lenebilir.** Teklif v2 ile sipariş v1 arasındaki fark, veya teklif v1 ile sipariş finali arasındaki fark — hepsi görülebilir.
5. **Kârlılık analizi:** Teklif finalindeki fiyatlar vs sipariş finalindeki gerçek maliyetler karşılaştırılarak kâr/zarar hesaplanır.

```
Örnek zincir:
v1 [teklif]  → v2 [teklif]  → v3 [teklif/kilitli] → v4 [sipariş] → v5 [sipariş/kilitli]
   müşteri       tasarım         teklif gönderildi      aşama geçişi     nihai tasarım
   ilk talep     revizyonu       kilitleme              (v3'ün kopyası)  final kilitleme
```

### 4.4 Fiyatlandırmada 3 Yöntem
1. Malzeme fiyatı × çarpan
2. Hacim hesabı × birim fiyat
3. Teorik imalat süresi × gün fiyatı

Üçü de hesaplanıp yan yana gösterilir. Geçmiş benzer projeler de aynı ekranda. Karar veren seçer.

### 4.5 Muhasebe Kapısı
> "Muhasebe okey vermeden üretime başlanmaması veya satın almanın yapılmaması." (01:55)

Uyarıyla esnetilebilir ama log tutulmalı.

### 4.6 İstasyon Renk Sistemi
- **Yeşil**: Önceki adım tamam + malzeme mevcut → yapılabilir
- **Sarı/Gri**: Önceki adım bitmedi VEYA malzeme gelmedi → beklemede
- **Mavi**: İşlem devam ediyor (barkod ile başlatıldı)
- **Kırmızı**: Hedef tarih geçmiş, hâlâ bitmemiş

### 4.7 Kısmi Sevkiyat & Faturalama
Aynı proje altındaki kalemler farklı tarihlerde sevk edilebilir. Aynı kalemin adetleri bile kısmi sevk edilebilir. Her sevk kendi faturasını tetikler.

### 4.8 ETA Entegrasyonu — Minimal & Periyodik
- **Çekilen**: Madde kartları (periyodik)
- **Gönderilen**: Onaylanan siparişler (fatura kesilmesi için)
- **İstenen**: Fatura/bakiye bilgisi (yönetim raporları için)
- API yok, SQL erişimi ile

---

## 5. GELECEĞİ ETKİLEYEN TASARIM KARARLARI

Mert'in "şu an istemiyoruz ama altyapısı olsun" dediği konular:

| Konu | Şu An | Gelecek | Tasarım Etkisi |
|------|-------|---------|----------------|
| Gerçek maliyet | Yok | Başla/bitir süreleri → gerçek maliyet | İş emrinde zaman damgası altyapısı şimdiden olmalı |
| Duruş kodları | Yok | Setup, elmas, arıza vb. | İş emri alt tablosu olarak düşünülmeli |
| Tezgah entegrasyonu | Yok | IoT sensör, tezgah duruyor/çalışıyor | İstasyon entity'sine tezgah_id alanı bırakılmalı |
| Metot süresi karşılaştırma | Yok | Teorik vs gerçek süre analizi | İş emrinde teorik_sure alanı şimdiden olmalı |
| Mail entegrasyonu | Soru işareti | Outlook SMTP veya program içi mail | Kullanıcıda email alanı, şablon yapısı hazır olmalı |
| Detaylı proses maliyetlendirme | Basit çarpan | İşlem bazlı maliyet (torna, freze ayrı) | İstasyon bazlı saat ücreti tanımlanabilir olmalı |

---

## 6. TOPLAM ENTITY SAYISI

| # | Entity | Tahmini Kayıt Hacmi (Yıllık) |
|---|--------|------------------------------|
| 1 | Firma | ~50-100 |
| 2 | Proje | ~200-500 |
| 3 | Kalem | ~500-2000 |
| 4 | BoyutParametreleri | = Kalem sayısı |
| 5 | AdminFormülleri | ~20-50 (az değişir) |
| 6 | MalzemeListesi | Kalem × 2-5 (UTA+USA+revizyonlar) |
| 7 | MalzemeKalemi | MalzemeListesi × 5-15 |
| 8 | MaddeKartı | ~1000-2000 (ETA'dan) |
| 9 | FiyatlandırmaÇalışması | = Kalem sayısı |
| 10 | SatınAlmaTalebi | MalzemeKalemi × ~1 |
| 11 | SatınAlmaSiparişi | ~2000-5000 |
| 12 | ProsesPaketi | ~15-30 (şablon) |
| 13 | ProsesAdımı | ProsesPaketi × 5-8 |
| 14 | İşEmri | Kalem × imalat_malzeme × proses_adım (~5000-20000) |
| 15 | FasonİşTakibi | İşEmri'nin %10-20'si |
| 16 | ProjeTakipAdımları | Kalem × ~14 adım |
| 17 | Kullanıcı | ~15-30 |
| 18 | PDFŞablonu | ~10-20 (statik) |

**Toplam: 18 entity, ~60.000-100.000 aktif kayıt/yıl tahmini**

---

*Bu veri modeli, 04.05.2026 tarihli toplantı transkriptinin satır satır analizinden çıkarılmıştır. Her alan ve iş kuralının yanında toplantıdaki referans zamanı belirtilmiştir.*
