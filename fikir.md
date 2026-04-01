<!DOCTYPE html>
<html lang="tr">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>TIBEXA — Website İçerik Stratejisi</title>
<link href="https://fonts.googleapis.com/css2?family=Cormorant+Garamond:ital,wght@0,400;0,600;1,400&family=DM+Sans:wght@300;400;500&display=swap" rel="stylesheet">
<style>
*, *::before, *::after { box-sizing: border-box; margin: 0; padding: 0; }

:root {
  --black: #06060a;
  --ink: #0e0e16;
  --iron: #22223a;
  --steel: #46465e;
  --silver: #8888a4;
  --frost: #ccccde;
  --white: #f2f2f6;
}

body {
  background: var(--black);
  color: var(--white);
  font-family: 'DM Sans', sans-serif;
  font-weight: 300;
  line-height: 1.8;
  font-size: 15px;
  padding: 0 0 6rem;
}

/* NAV */
.top-nav {
  display: flex;
  justify-content: space-between;
  align-items: center;
  padding: 2rem 3.5rem;
  border-bottom: 0.5px solid var(--iron);
  position: sticky;
  top: 0;
  background: var(--black);
  z-index: 10;
}
.nav-logo {
  font-family: 'Cormorant Garamond', serif;
  font-size: 16px;
  font-weight: 600;
  letter-spacing: 0.1em;
  color: var(--frost);
}
.nav-meta {
  font-size: 11px;
  letter-spacing: 0.12em;
  text-transform: uppercase;
  color: var(--steel);
}

/* HERO */
.doc-hero {
  padding: 5rem 3.5rem 4rem;
  border-bottom: 0.5px solid var(--iron);
  max-width: 760px;
}
.doc-kicker {
  font-size: 10px;
  letter-spacing: 0.18em;
  text-transform: uppercase;
  color: var(--steel);
  margin-bottom: 1.25rem;
}
.doc-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: clamp(32px, 5vw, 52px);
  font-weight: 600;
  line-height: 1.1;
  color: var(--frost);
  margin-bottom: 1.5rem;
}
.doc-intro {
  font-size: 15px;
  font-weight: 300;
  color: var(--silver);
  max-width: 600px;
  line-height: 1.8;
}

/* SECTION */
.section {
  padding: 3.5rem 3.5rem 0;
  max-width: 860px;
}

.section-header {
  display: flex;
  align-items: baseline;
  gap: 1.5rem;
  margin-bottom: 2.5rem;
  padding-bottom: 1.25rem;
  border-bottom: 0.5px solid var(--iron);
}
.section-num {
  font-size: 10px;
  letter-spacing: 0.16em;
  text-transform: uppercase;
  color: var(--steel);
  flex-shrink: 0;
}
.section-name {
  font-family: 'Cormorant Garamond', serif;
  font-size: 24px;
  font-weight: 600;
  color: var(--frost);
}
.section-tag {
  font-size: 10px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  color: var(--steel);
  border: 0.5px solid var(--iron);
  padding: 3px 10px;
  border-radius: 3px;
  margin-left: auto;
}

/* CONTENT BLOCKS */
.block {
  margin-bottom: 2.5rem;
}
.block-label {
  font-size: 10px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--steel);
  margin-bottom: 0.75rem;
}
.block-title {
  font-family: 'Cormorant Garamond', serif;
  font-size: 19px;
  font-weight: 600;
  color: var(--frost);
  margin-bottom: 0.75rem;
  font-style: italic;
}
.block-body {
  font-size: 14px;
  font-weight: 300;
  color: var(--silver);
  line-height: 1.85;
  max-width: 640px;
}
.block-body p + p { margin-top: 0.75rem; }

/* COPY EXAMPLE */
.copy-example {
  background: var(--ink);
  border-left: 2px solid var(--iron);
  padding: 1.25rem 1.5rem;
  margin: 1rem 0 1.5rem;
  border-radius: 0 4px 4px 0;
}
.copy-example-label {
  font-size: 9px;
  letter-spacing: 0.14em;
  text-transform: uppercase;
  color: var(--steel);
  margin-bottom: 0.6rem;
}
.copy-example-text {
  font-family: 'Cormorant Garamond', serif;
  font-size: 17px;
  font-weight: 400;
  font-style: italic;
  color: var(--frost);
  line-height: 1.5;
}

/* ANTI COPY */
.anti-copy {
  background: var(--ink);
  border-left: 2px solid #2a2a3a;
  padding: 1.25rem 1.5rem;
  margin: 1rem 0 1.5rem;
  border-radius: 0 4px 4px 0;
}
.anti-copy .copy-example-text {
  color: var(--steel);
  text-decoration: line-through;
  text-decoration-color: var(--iron);
}

/* RULE LIST */
.rule-list {
  display: flex;
  flex-direction: column;
  gap: 10px;
  margin-top: 1rem;
}
.rule-item {
  display: flex;
  gap: 14px;
  font-size: 13px;
  font-weight: 300;
  color: var(--silver);
  line-height: 1.6;
}
.rule-item::before {
  content: attr(data-mark);
  color: var(--iron);
  flex-shrink: 0;
  font-size: 13px;
  margin-top: 1px;
}
.rule-item.yes { color: #7a9880; }
.rule-item.yes::before { color: #3a5e42; }

/* PAGE MAP */
.page-map {
  display: flex;
  flex-direction: column;
  gap: 2px;
  margin-top: 1.5rem;
}
.page-row {
  display: grid;
  grid-template-columns: 140px 1fr 100px;
  gap: 1.5rem;
  padding: 1rem 1.25rem;
  background: var(--ink);
  border-radius: 3px;
  align-items: start;
}
.page-row-name {
  font-size: 13px;
  font-weight: 500;
  color: var(--frost);
}
.page-row-desc {
  font-size: 12px;
  font-weight: 300;
  color: var(--silver);
  line-height: 1.6;
}
.page-row-priority {
  font-size: 9px;
  letter-spacing: 0.1em;
  text-transform: uppercase;
  text-align: right;
}
.p-core { color: #7a9880; }
.p-second { color: #6e6e88; }
.p-later { color: #3e3e54; }

/* DIVIDER */
.divider { margin: 3.5rem 3.5rem 0; height: 0.5px; background: var(--iron); }

/* PRINCIPLE CARDS */
.principles {
  display: grid;
  grid-template-columns: 1fr 1fr;
  gap: 2px;
  margin-top: 1.5rem;
}
.principle {
  background: var(--ink);
  padding: 1.5rem 1.75rem;
}
.principle-num {
  font-family: 'Cormorant Garamond', serif;
  font-size: 36px;
  font-weight: 600;
  color: var(--iron);
  line-height: 1;
  margin-bottom: 0.5rem;
}
.principle-title {
  font-size: 13px;
  font-weight: 500;
  color: var(--frost);
  margin-bottom: 0.5rem;
}
.principle-body {
  font-size: 12px;
  font-weight: 300;
  color: var(--silver);
  line-height: 1.7;
}

@media (max-width: 700px) {
  .top-nav, .doc-hero, .section, .divider { padding-left: 1.5rem; padding-right: 1.5rem; }
  .page-row { grid-template-columns: 1fr; gap: 0.5rem; }
  .page-row-priority { text-align: left; }
  .principles { grid-template-columns: 1fr; }
}
</style>
</head>
<body>

<nav class="top-nav">
  <div class="nav-logo">TIBEXA</div>
  <div class="nav-meta">Website İçerik Stratejisi</div>
</nav>

<!-- HERO -->
<div class="doc-hero">
  <div class="doc-kicker">İçerik Mimarisi · Kopya Stratejisi · Sayfa Yapısı</div>
  <h1 class="doc-title">Sitede ne yazmalı, nasıl yazmalı</h1>
  <p class="doc-intro">
    Bu döküman TIBEXA'nın web sitesinde hangi sayfaların olması gerektiğini, her sayfada ne söylenmesi gerektiğini ve nasıl bir dil kullanılması gerektiğini anlatıyor. Tasarımdan önce içerik — her zaman.
  </p>
</div>


<!-- ═══════════════════════════════
     01 — SAYFA MİMARİSİ
═══════════════════════════════ -->
<div class="section">
  <div class="section-header">
    <span class="section-num">01</span>
    <span class="section-name">Sayfa Mimarisi</span>
    <span class="section-tag">Yapı</span>
  </div>

  <div class="block">
    <div class="block-label">Hangi sayfalar olmalı</div>
    <div class="block-body">
      <p>Site yalın olmalı. 10 sayfalık karmaşık bir navigasyon değil, her sayfanın bir tek işi var. Ziyaretçi kaybolmuyor — ya devam ediyor ya çıkıyor.</p>
    </div>
  </div>

  <div class="page-map">
    <div class="page-row">
      <div class="page-row-name">Ana Sayfa</div>
      <div class="page-row-desc">Kim olduğunuz, kim için çalıştığınız, ne yapıyorsunuz — 90 saniyede anlatılıyor. Tek CTA: strateji görüşmesi.</div>
      <div class="page-row-priority p-core">Kritik</div>
    </div>
    <div class="page-row">
      <div class="page-row-name">Metodoloji</div>
      <div class="page-row-desc">GTM sisteminizi, süreci ve neden farklı olduğunuzu derinlemesine anlatıyorsunuz. Rakip farkını burada kanıtlıyorsunuz.</div>
      <div class="page-row-priority p-core">Kritik</div>
    </div>
    <div class="page-row">
      <div class="page-row-name">Kimler İçin</div>
      <div class="page-row-desc">Çalıştığınız profili açıkça tanımlıyorsunuz. Hem eliyor hem mıknatıs görevi görüyor. "Bu benim" hissini yaratıyor.</div>
      <div class="page-row-priority p-core">Kritik</div>
    </div>
    <div class="page-row">
      <div class="page-row-name">Vaka Çalışmaları</div>
      <div class="page-row-desc">Rakam var, isim var (izin alındıysa), süreç var, sonuç var. "Bunu söylüyorlar" değil "bunu kanıtlıyorlar" formatı.</div>
      <div class="page-row-priority p-core">Kritik</div>
    </div>
    <div class="page-row">
      <div class="page-row-name">İçgörüler / Blog</div>
      <div class="page-row-desc">B2B ihracat, GTM, outbound üzerine orijinal bakış açısı. SEO değil düşünce liderliği hedefleniyor. Ayda 2-4 yazı yeterli.</div>
      <div class="page-row-priority p-second">Önemli</div>
    </div>
    <div class="page-row">
      <div class="page-row-name">Hakkımızda</div>
      <div class="page-row-desc">Kuru CV değil, kurucunun hikayesi ve bakış açısı. Neden bu işi yapıyorsunuz, neden şimdi, neden bu şekilde.</div>
      <div class="page-row-priority p-second">Önemli</div>
    </div>
    <div class="page-row">
      <div class="page-row-name">İletişim / Başvuru</div>
      <div class="page-row-desc">Basit form. Ama birkaç eleme sorusu içeriyor — "hangi pazara açılmak istiyorsunuz, yıllık ihracat hacminiz" gibi. Zamanınızı korur.</div>
      <div class="page-row-priority p-second">Önemli</div>
    </div>
    <div class="page-row">
      <div class="page-row-name">Araçlar / Kaynaklar</div>
      <div class="page-row-desc">Lead manyeti: ICP şablonu, GTM checklist, pazar önceliklendirme matrisi. İndirmek için email yeterli.</div>
      <div class="page-row-priority p-later">Sonraki aşama</div>
    </div>
  </div>
</div>


<!-- ═══════════════════════════════
     02 — ANA SAYFA
═══════════════════════════════ -->
<div class="divider"></div>
<div class="section">
  <div class="section-header">
    <span class="section-num">02</span>
    <span class="section-name">Ana Sayfa — Bölüm Bölüm</span>
    <span class="section-tag">Kopya</span>
  </div>

  <div class="block">
    <div class="block-label">Hero — ilk ekran</div>
    <div class="block-title">Bir cümle, bir karar</div>
    <div class="block-body">
      <p>Ziyaretçinin %70'i hero'da karar veriyor: "devam mı, çık mı." Başlık ne iş yaptığınızı değil, ziyaretçinin ne kazanacağını söylemeli. Alt başlık kim için olduğunu netleştirmeli. CTA tek ve açık olmalı.</p>
    </div>

    <div class="copy-example">
      <div class="copy-example-label">Örnek başlık yönü</div>
      <div class="copy-example-text">"Uluslararası alıcı bulmak şans işi değil. Sistem işi."</div>
    </div>
    <div class="copy-example">
      <div class="copy-example-label">Alternatif</div>
      <div class="copy-example-text">"B2B ihracatta ilk toplantıyı bulmak değil, doğru toplantıyı bulmak."</div>
    </div>
    <div class="anti-copy">
      <div class="copy-example-label">Kaçınılacak</div>
      <div class="copy-example-text">"Sürdürülebilir büyüme için stratejik ortağınız."</div>
    </div>

    <div class="block-body">
      <p>Alt başlık 2 cümle. Kim olduğunuzu değil, kimin sorununu çözdüğünüzü söylüyor. "ROI odaklı ihracatçı firmalar için outbound satış altyapısı kuruyoruz" gibi — spesifik, kişi hissettiriyor.</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Metrik şeridi</div>
    <div class="block-title">Sayılar konuşuyor</div>
    <div class="block-body">
      <p>Hero'nun hemen altında 3-4 rakam. Bunlar sosyal kanıt değil, kalibrasyon. Ziyaretçi "bunlar benim boyutumda mı çalışıyor" sorusunu burada cevaplıyor. Rakamlar spesifik ve gerçek olmalı — yuvarlak sayılar güven kırıyor.</p>
    </div>
    <div class="rule-list">
      <div class="rule-item yes" data-mark="✓">Toplam müşteri ihracat hacmi büyümesi (dolar bazında)</div>
      <div class="rule-item yes" data-mark="✓">Ortalama satış döngüsü kısalması (hafta veya yüzde)</div>
      <div class="rule-item yes" data-mark="✓">Aktif pazar sayısı veya ülke</div>
      <div class="rule-item yes" data-mark="✓">Yenileme / devam oranı</div>
      <div class="rule-item" data-mark="✗">Müşteri sayısı — küçük rakamlar güven değil soru işareti yaratır</div>
      <div class="rule-item" data-mark="✗">"10 yıllık deneyim" — bu sizi değil zamanı anlatıyor</div>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Yöntem özeti</div>
    <div class="block-title">Nasıl çalışıyorsunuz — kısa versiyon</div>
    <div class="block-body">
      <p>3 adım veya 3 katman. Her biri bir başlık + 2 cümle. Burada sisteminizi satmıyorsunuz, merak yaratıyorsunuz. "Bunu nasıl yapıyorsunuz?" sorusunu "Metodoloji" sayfasına yönlendiriyor.</p>
      <p>Her adım eylem fiiliyle başlamalı: "Haritalıyoruz / Kuruyoruz / Ölçüyoruz." Pasif değil, aktif. Danışman değil operatör hissi.</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">ICP sinyali</div>
    <div class="block-title">Kimlerle çalışmıyorsunuz — cesur hamle</div>
    <div class="block-body">
      <p>Ana sayfada çalıştığınız profili tanımlamak standart. Ama çalışmadığınız profili de netleştirmek cesur ve güçlü. Bu hem eliyor hem doğru kişiyi çekiyor. "Sizinle çalışmıyor olabiliriz" cümlesi doğru alıcıya "tam bunları arıyorum" hissini verir.</p>
    </div>
    <div class="copy-example">
      <div class="copy-example-label">Örnek yön</div>
      <div class="copy-example-text">"Her ihracatçıyla çalışmıyoruz. ROI'yi maliyet değil fırsat olarak görenlerle çalışıyoruz."</div>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Vaka önizlemesi</div>
    <div class="block-title">Bir sonuç, somut</div>
    <div class="block-body">
      <p>Ana sayfada bir tam vaka değil, bir sonuç parçası. Sektör + rakam + zaman dilimi. İsim gizlenebilir, sayı gizlenmemeli. "Bir Türk tekstil ihracatçısı 6 ayda Almanya'da 3 yeni hesap açtı" gibi — okuyucu kendi ülkesini ve sektörünü hayal ediyor.</p>
    </div>
  </div>
</div>


<!-- ═══════════════════════════════
     03 — METODOLOJİ SAYFASI
═══════════════════════════════ -->
<div class="divider"></div>
<div class="section">
  <div class="section-header">
    <span class="section-num">03</span>
    <span class="section-name">Metodoloji Sayfası</span>
    <span class="section-tag">Derinlik</span>
  </div>

  <div class="block">
    <div class="block-label">Bu sayfanın görevi</div>
    <div class="block-body">
      <p>Metodoloji sayfası fiyat öncesinin son duvarı. Buraya gelen ziyaretçi ciddi. Bu sayfa "nasıl çalışıyorsunuz" sorusunu cevaplıyor ama asıl işi "rakiplerden neden farklısınız" sorusunu cevaplamak.</p>
      <p>Jenerik süreç anlatımı burada öldürücü. "Analiz ederiz, strateji geliştiririz, uygularız" herkes yazıyor. Siz ne yapıyorsunuz ki başkası yapamıyor?</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">İçerik yapısı</div>
    <div class="block-body">
      <p>Sayfayı üç katmana bölün. İlk katman neden bu metodolojiye ihtiyaç var — piyasadaki sorun ne. İkinci katman sisteminizin 3-4 ana bileşeni, her biri için ne yaptığınız ve neden önemli olduğu. Üçüncü katman bu sistemin çıktısı — müşteri ne görüyor, ne ölçüyor.</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Psikografik alıcı haritası</div>
    <div class="block-title">Bunu açıkça yazın</div>
    <div class="block-body">
      <p>Metodolojinizin kalbinde psikografik segmentasyon var — bunu sır gibi saklamayın, avantaja çevirin. Rakipler demografik ve sektörel bakıyor. Siz zihin yapısına bakıyorsunuz. Bu farkı sayfada gösterin, terminolojinizi öğretin. "Psikografik ICP" kavramını siz öğrettiyseniz, alıcı sizi hatırlıyor.</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Rakip karşılaştırma</div>
    <div class="block-title">İsim vermeden konumlanın</div>
    <div class="block-body">
      <p>Rakip isim vermek riskli, ama "geleneksel yaklaşım vs. TIBEXA yaklaşımı" formatı güçlü. İki sütun: biri reaktif, veri yoksun, kampanya bazlı. Diğeri proaktif, ölçülebilir, sistem bazlı. Okuyucu zaten hangi tarafta olduğunu biliyor.</p>
    </div>
  </div>
</div>


<!-- ═══════════════════════════════
     04 — KİMLER İÇİN
═══════════════════════════════ -->
<div class="divider"></div>
<div class="section">
  <div class="section-header">
    <span class="section-num">04</span>
    <span class="section-name">Kimler İçin Sayfası</span>
    <span class="section-tag">Eleme + Çekim</span>
  </div>

  <div class="block">
    <div class="block-label">Bu sayfanın stratejik değeri</div>
    <div class="block-body">
      <p>Bu sayfa satmıyor — eliyor. Ve eleme satışın en ucuz yollarından biri. Yanlış müşteriye harcanan zaman, doğru müşteriyi kaybettiren zamandır. Bu sayfayı cesurca yazın.</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">İki blok yan yana</div>
    <div class="block-body">
      <p>Sol blok: çalıştığınız profilin zihin yapısı. Sadece sektör veya firma büyüklüğü değil — nasıl düşünüyor, neye değer veriyor, hangi soruyu soruyor. Sağ blok: çalışmadığınız profil. Aynı format, ama tersi. Bu ikisi yan yana durduğunda okuyucu hangisi olduğunu biliyor.</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Sektör ve boyut</div>
    <div class="block-body">
      <p>Hangi sektörlerde sonuç ürettiğinizi netleştirin — ama sektörü değil problemi tanımlayın. "Tekstil firmaları" değil "kurumsal alıcıya uzun satış döngüsüyle çalışan ihracatçılar." Bu tarif çok daha geniş bir profili çeker ve aynı zamanda daha doğru bir eşleşme sağlar.</p>
    </div>
  </div>
</div>


<!-- ═══════════════════════════════
     05 — VAKA ÇALIŞMALARI
═══════════════════════════════ -->
<div class="divider"></div>
<div class="section">
  <div class="section-header">
    <span class="section-num">05</span>
    <span class="section-name">Vaka Çalışmaları</span>
    <span class="section-tag">Kanıt</span>
  </div>

  <div class="block">
    <div class="block-label">Vaka anatomisi</div>
    <div class="block-body">
      <p>Her vaka aynı yapıyı takip ediyor: müşteri profili (isim veya anonim), başlangıç problemi (rakamla), TIBEXA'nın ne yaptığı (adım adım değil özet), sonuç (rakamla ve zaman dilimiyle), müşterinin kendi cümlesi (opsiyonel ama güçlü).</p>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Rakam kuralı</div>
    <div class="block-body">
      <p>Her vakada en az 2 somut rakam olmalı: bir başlangıç noktası, bir sonuç noktası. "Significiant büyüme sağladık" cümlesi bu sayfada işe yaramaz. "%340 pipeline büyümesi, 5 ayda" çalışır.</p>
    </div>
    <div class="rule-list">
      <div class="rule-item yes" data-mark="✓">"Pipeline değeri 6 ayda $2.4M'dan $8.1M'a çıktı"</div>
      <div class="rule-item yes" data-mark="✓">"Almanya pazarında ilk 90 günde 14 nitelikli toplantı"</div>
      <div class="rule-item yes" data-mark="✓">"Satış döngüsü 9 haftadan 4 haftaya indi"</div>
      <div class="rule-item" data-mark="✗">"Hızlı ve etkili sonuçlar aldık"</div>
      <div class="rule-item" data-mark="✗">"Müşterimiz çok memnun kaldı"</div>
    </div>
  </div>

  <div class="block">
    <div class="block-label">Kaç vaka</div>
    <div class="block-body">
      <p>Başlangıç için 3 yeterli. 3 farklı sektör veya pazar olsun — çeşitlilik güven yaratır. Zamanla 5-6'ya çıkar. 20 vaka sizi büyük göstermez, seçici görünmemenizi sağlar.</p>
    </div>
  </div>
</div>


<!-- ═══════════════════════════════
     06 — DİL PRENSİPLERİ
═══════════════════════════════ -->
<div class="divider"></div>
<div class="section">
  <div class="section-header">
    <span class="section-num">06</span>
    <span class="section-name">Dil ve Ton Prensipleri</span>
    <span class="section-tag">Ses</span>
  </div>

  <div class="block">
    <div class="block-label">TIBEXA nasıl konuşur</div>
    <div class="block-body">
      <p>Sitenin her kelimesi aynı sesi taşımalı. Bu ses ne çok akademik ne çok günlük. Kesin, direkt, sakin ve kanıta dayalı. Heyecan sizi küçülttür — sonuçlar konuşur, siz değil.</p>
    </div>
  </div>

  <div class="principles">
    <div class="principle">
      <div class="principle-num">01</div>
      <div class="principle-title">Aktif fiil, her zaman</div>
      <div class="principle-body">"Yardımcı oluyoruz" değil "kuruyoruz." "Destek sağlıyoruz" değil "açıyoruz." Pasif fiil belirsizlik, aktif fiil taahhüt.</div>
    </div>
    <div class="principle">
      <div class="principle-num">02</div>
      <div class="principle-title">Rakam olmadan iddia yok</div>
      <div class="principle-body">Her iddiayı bir sayı takip eder. Sayı yoksa cümle silinir veya somutlaştırılır. "Hızlı" değil "ortalama 6 haftada."</div>
    </div>
    <div class="principle">
      <div class="principle-num">03</div>
      <div class="principle-title">Jargon değil, terminoloji</div>
      <div class="principle-body">"Sinerjik büyüme" jargon. "Pipeline velocity" terminoloji — hedef kitleniz biliyor, sahiplenilmesi güç. Farkı koruyun.</div>
    </div>
    <div class="principle">
      <div class="principle-num">04</div>
      <div class="principle-title">Soru sormak satışı başlatır</div>
      <div class="principle-body">Her bölümün sonunda ziyaretçiye bir soru bırakın — cevaplamak için bir sonraki sayfaya geçsin ya da iletişime geçsin. "Sizin ICP'niz ne kadar net?" gibi.</div>
    </div>
    <div class="principle">
      <div class="principle-num">05</div>
      <div class="principle-title">Kısa paragraf, uzun fikir</div>
      <div class="principle-body">Web'de 3 satırı aşan paragraf okunmuyor. Fikir derin olabilir, cümle kısa olabilir. Çelişmiyor.</div>
    </div>
    <div class="principle">
      <div class="principle-num">06</div>
      <div class="principle-title">Tek CTA kuralı</div>
      <div class="principle-body">Her sayfada tek bir birincil aksiyon. "Ya bunu yap ya şunu yap" ziyaretçiyi felç eder. Strateji görüşmesi mi, kaynak indir mi — seçin, tutun.</div>
    </div>
  </div>
</div>


<!-- ═══════════════════════════════
     07 — NE YAZILMAMALI
═══════════════════════════════ -->
<div class="divider"></div>
<div class="section" style="padding-bottom:0;">
  <div class="section-header">
    <span class="section-num">07</span>
    <span class="section-name">Kesinlikle Yazılmamalı</span>
    <span class="section-tag">Kırmızı çizgiler</span>
  </div>

  <div class="block">
    <div class="rule-list">
      <div class="rule-item" data-mark="✗">"360 derece çözümler sunuyoruz" — anlamsız, herkes yazıyor</div>
      <div class="rule-item" data-mark="✗">"Müşteri odaklı yaklaşım" — aksini kim iddia eder ki</div>
      <div class="rule-item" data-mark="✗">"Sektörde X yıllık deneyim" — deneyim sonuç değil, araç</div>
      <div class="rule-item" data-mark="✗">"Vizyonumuz, misyonumuz, değerlerimiz" bölümleri — bunları kimse okumaz, eylemle gösterin</div>
      <div class="rule-item" data-mark="✗">Stok fotoğraf — el sıkışan insanlar, ofis toplantıları, dünya haritası görselleri</div>
      <div class="rule-item" data-mark="✗">"Hemen iletişime geçin!" — acelecilik ucuzlatır</div>
      <div class="rule-item" data-mark="✗">Referans logoları güven yaratmaz, çalıştığınız firmaların büyüklüğünü bir rakamla anlatın</div>
      <div class="rule-item" data-mark="✗">"Biz en iyiyiz" iddiası — en iyiyseniz bunu müşterileriniz söyler, siz değil</div>
    </div>
  </div>
</div>

</body>
</html>