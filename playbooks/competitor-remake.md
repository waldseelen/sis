# Rakip Outlier Analizi ve Özgün Yeniden Yapım (`competitor-remake`)

Bu iş akışı, kanıtlanmış rakiplerden öğrenip YouTube tekrarlayan/kopya içerik cezasına yakalanmadan daha güçlü versiyon üretmek içindir.

---

## Adım 1 — Outlier Rakip Bulma (Gizli Sekme)

1. Tarayıcıyı **gizli sekmede** aç (kişisel geçmiş algoritmayı bozmasın).
2. Hedef niş anahtar kelimesini ara ve filtrele:
   - **Sıralama:** Görüntüleme sayısı / Popülerlik
   - **Yükleme Tarihi:** Son 1 yıl
   - *(Shorts kanalıysa)* **Süre:** 4 dakikadan kısa
3. **Aranan Sinyal:**
   - Düşük aboneli ama abone sayısından çok daha yüksek izlenme almış **outlier** kanal (ör. 22K aboneyle 25M izlenme veya 170K aboneyle 50M izlenme), VE
   - Nişteki en eski, en kıdemli, en yüksek izlenmeli ana kanal.
4. Sadece izlenmeye bakma; **ses tonunu, görsel stilini, altyazıyı, ilk 10 sn kancayı, başlığı ve küçük resmi** birlikte analiz et.

---

## Adım 2 — Yerel Transkript Çekimi (`yt-dlp`, Harici Site Gereksiz)

Üçüncü parti web sitelerine (`youtubetotranscript` vb.) bağımlı kalmadan yerel `yt-dlp` ile temiz altyazı/meta veri çekilir:

```bash
# Otomatik veya manuel altyazıyı sadece metin olarak indir (video indirmeden)
yt-dlp --skip-download --write-auto-sub --write-sub --sub-lang en --sub-format srt -o "rakip_%(id)s" "<VIDEO_URL>"

# Rakip başlık, açıklama ve etiket yapısını incele
yt-dlp --dump-json --skip-download "<VIDEO_URL>" > rakip_meta.json
```

---

## Adım 3 — Özgünleştirme ve Yeniden Yazım Kuralları

1. **Anlam & Tema Sadakati:** Rakip videonun neden tuttuğunu (ana vaat, psikolojik kanca, açık döngü sırası) koru.
2. **Sert Değişiklik Zorunluluğu:**
   - Hiçbir cümleyi olduğu gibi bırakma; **isimleri, yerleri, mekanları ve örnekleri değiştir**.
   - Metin tonunu hedefine göre yeniden kur (resmiyse daha samimi, tekdüzeyse daha sürükleyici ve arkadaş canlısı).
   - Yapay zekâdan alınan ham çıktıyı olduğu gibi kullanma; kendi özgün dokunuşunu, vurgularını ve bakış açını ekle (YouTube ham AI kalıbını ayırt edebilir).
3. **Çeviri / Çapraz Dil Avantajı:**
   - Başka dilde (ör. İspanyolca/Almanca/Türkçe/İngilizce) tutmuş bir fikri hedef dile çevirirken bile cümleleri yerelleştirip yeniden yaz.
   - Başlığı YouTube'da arat: birebir aynısının henüz olmaması avantajdır.

---

## Adım 4 — Küçük Resimde Minimum 2 Fark Kuralı

1. Rakibin en çok tıklanan kapağının **kompozisyon mantığını** incele (odak nesne, yüz/silüet, 3–4 kelime konumlandırması).
2. Kendi kapağında **en az 2 belirgin ögeyi değiştir**:
   - Daha güçlü renk kontrastı (karanlık arka plan + keskin vurgu),
   - Rakip kapakta olmayan en az 2 görsel öge/sembol veya farklı görsel tarz,
   - Aynı kelimeleri kopyalamadan daha yüksek merak boşluğu oluşturan 3–4 kelimelik metin.
3. Kontrol: `python3 core/scripts/yt_title_lint.py --title "<BASLIK>" --thumb "<KAPAK_METNI>" --json`
