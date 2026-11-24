# YouTube Büyüme, Hook, Paketleme ve Yayın Oyun Kitabı

Bu rehber, 0 → 1000+ abone ve kalıcı gelir (evergreen + yüksek retention) için bağlayıcı strateji standartlarını belirler.

---

## 1. Fikir Seçimi, Niş Harmanlama ve Doğrulama

1. **Kanıtlanmış Fikir Kuralı:** Sıfırdan riskli fikir uydurma; başka dillerde bile olsa son 1 yılda tuttuğu kanıtlanmış fikirleri esas al.
2. **Niş Daraltma & Harmanlama (Ikigai + Sıfır Rekabet):**
   - Ana konuyu benzer bir yan nişle harmanla (ör. **Stoacılık + Disiplin + Meditasyon**).
   - İki alanın en çok izlenen kanallarını ve en popüler videolarını bulup tek kanalda birleştirerek iki kitleyi birden al.
   - **Evergreen önceliği:** Her zaman aranan, zamansız konular seç (Stoacılık, temel finans, sağlık, uyku/meditasyon).
   - **Yatay TV & Yaşlı İzleyici Avantajı:** Videolar televizyondan yoğun izlendiği için 16:9 yatay yüksek çözünürlük (mümkünse 4K / keskin 1080p+) ve uzun süreler avantaj sağlar; yaşlı kitle videoları sonuna kadar izleme eğilimindedir.
3. **Triple-C & Fikir Çiftçiliği:**
   - Rakip kanalları tara → içerik türlerini kategorize et → en çok izlenen 3–5 formatı çıkar → 3 aylık içerik takvimini ilk videoyu bile çekmeden planla.
4. **Fikir Eleme Filtresi (4 Soru):**
   - Bu fikrin izlendiğine dair somut kanıt var mı?
   - **Google Trends → YouTube Arama** filtresinde gerçek talep ve kitle görünüyor mu?
   - Mevcut imkânlarla haftada en az 1 video tutarlılığıyla sürdürülebilir mi?
   - Başlık + kapak + akış tek pakete dönüşebiliyor mu?
   - En değerli fikir: *Yüksek başarı olasılığı × kısa süre × düşük üretim eforu* (örn. Stoic Discipline).

---

## 2. Hook, Retention (%92 Hedefi) ve Senaryo Omurgası

> **Temel Kural:** İzlenme sayısını belirleyen ana etken kamera veya ağır edit değil, **fikir + kanca + senaryo akışıdır**.

### İlk 2–3 Saniye ve İlk 10 Saniye
- **3'lü Kanca:** İlk saniyede **işitsel** (vurucu cümle) + **görsel** (merak ettiren sahne/simge) + **yazımsal** (ekranda destek metni) birlikte vurur.
- **Başlık & Kapak Doğrulaması:** Giriş, thumbnail ve başlığın vaadini anında karşılar; izleyici yanlış yere geldiğini hissetmez.
- **Basitlik & Duygu:** Bir çocuğun bile anlayacağı netlikte, **"sen"** diliyle ve ilk cümleden duygu tetikleyerek doğrudan konuya gir (**önce aksiyon, sonra bağlam**).
- Puanlama komutu: `python3 core/scripts/yt_hookscore.py --hook "<ilk cumle>" --json`

### HPC Sistemi & Açık Döngüler (Open Loops)
1. **H (Hook):** Merak boşluğu aç, videoyu bitirince ne kazanacağını net söyle, benzersizliği/araştırma emeğini/kanıtı göster.
2. **P (Progression — Damla Damla Bağlam):**
   - İzleyiciyi erken ve zamansız ödüllendirme.
   - Bir soruyu çözerken yeni bir açık döngü aç; ritmi, vurguyu ve tonlamayı canlı tut (tekdüze robotik okuma yapma, sohbet/sinema anlatımı kur).
   - **4 Parçalı Seri Girişi:** (1) Selamlama → (2) Tek cümleyle serinin/olayın özeti → (3) Güncelleme → (4) İlk hedef (önceki bölümü izlemeyen bile anlasın).
3. **C (Climax & Son Cümle Köprüsü):**
   - Vaat edilen esas ödülü videonun sonunda ver ve izleyiciyi tatmin et.
   - **Son Cümle Köprüsü:** Video biterken yeni bir soru/problem aç ve çözümünün kanalındaki bir sonraki videoda olduğunu vaat et (otomatik sonraki videoya geçiş).

---

## 3. Thumbnail + Başlık + VSL Paketlemesi

### Thumbnail (Küçük Resim) Kuralları
- **Sadelik:** Karmaşık grafik/logo kalabalığını at. Tek konu + duygu/simge + **3–4 kelimelik** kalın, yüksek kontrastlı metin.
- **Merak Boşluğu (FOMO):** İzleyicinin bildiği ile bilmediği arasında köprü kur; imkânsız veya çarpıcı görünen bir iddiayı görselleştir.
- **Renk Uyumu:** Videonun iç renk paletiyle uyumlu olsun (seri bölümlerde mavi/yeşil gibi tutarlı vurgu paletleri).
- **Tekrar Yasağı:** Başlıkta geçen kelimeleri thumbnail yazısında tekrar etme (`python3 core/scripts/yt_title_lint.py`).

### Açıklama, VSL Stratejisi ve SEO
- **VSL (Virtual Sales Letter) Tek Link Kuralı:** Kanaldaki en ikna edici, abone olmaya ve ürüne/sonraki adıma en çok yönlendiren tek bir "ana video" belirlenir; diğer tüm videoların açıklamasına **yalnızca bu tek link** konur (dış Instagram/X/Facebook linkleri sadece kanal biyografisinde kalır — izleyiciyi YouTube dışına kaçırma).
- **Altın İlk 2 Satır:** Açıklamanın ilk 2 satırı anahtar kelimelerle videoyu özetlemelidir.
- **Gerçek Chapter Başlıkları:** "Giriş / Gelişme / Sonuç" değil, o an videoda tam olarak ne anlatıldığını yaz (`00:00` ile başla, >=3 bölüm, >=10 sn — `core/scripts/caption_and_chapters.py`).
- **Oynatma Listeleri:** Arama motoru gibi konu kümelerine ayır.
- **Küresel Erişim:** Farklı dillerde `.srt` altyazı ekle (`en`, `es`, `de`, `tr`) ve YouTube Studio'da **otomatik dublajı** aktif et.

---

## 4. Kanal Sağlığı, Yükleme ve Yayın Sonrası Disiplin

- **1000 İzlenme Altı Koruması (Bot Gibi Görünme):**
  - Sıfır yeni mail ile hemen video atma; hesaptan daha önce izleme, beğeni, yorum yaparak doğal geçmiş oluştur.
  - Kanal ayarlarını (genel niş anahtar kelimeleri, yükleme varsayılanlarında 3 soru: *ne hakkında, kime yardım, hangi konular*, SEO ağırlıklı uzun Hakkında yazısı, profil & banner) yaptıktan sonra **1–2 gün bekle**.
- **Yükleme Protokolü:**
  1. Önce **`private` (gizli)** yükle, 1–2 saat beklet.
  2. YouTube Studio → Analiz → İzleyicilerin YouTube'da olduğu zamanlar (mor alan) → zirve saatten **~1 saat önce** ve **çeyrek geçe (`:15` veya `:45`)** yayına al.
- **Yayın Sonrası Yapılmayacaklar:**
  - Kendi videonu açıp 5–10 sn bakıp çıkma (ilk izleyicilerden biri sensin; retention düşer).
  - Sonuna kadar izlemeyecek eş/dost/gruba link atma.
  - 2–3 haftadan önce başlık/thumbnail değiştirme; erken kaos verisine göre video silme (bazı videolar aylar sonra patlar).
  - Asla izlenme/abone satın alma.
  - Shorts (`<=59 sn`) ve uzun videoları aynı kanala karıştırma.
- **Topluluk & Monetizasyon:**
  - Sabit yoruma tartışma başlatacak soru sabitle; yorum yapanlara samimi yanıt verip karşı soru sor (sesli yanıt özelliği dahil); kötü yorum varsa iyi yorumlara cevap verip üste taşı.
  - Doğrudan gelir için 4 sütun: **kurslar, koçluk, danışmanlık, dijital ürünler**.
