# CLAUDE.md — `sis` YouTube Stüdyosu Bağlayıcı Kuralları

Bu depo **12 yüzsüz/anlatımlı YouTube kanalını** yönetmek için hazırlanmış üretim stüdyosudur. Çekirdek skill'ler, scriptler ve kalite kapıları `core/` alt modülünden (`waldseelen/CONTENTY`) gelir.

---

## §0. Oturum Başlangıcı ve Okuma Sırası (Zorunlu)

Herhangi bir üretim, analiz veya kod değişikliği öncesi sırayla oku:
1. `CLAUDE.md` (bu dosya)
2. `ARCHITECTURE.md` ve `SPEC.md`
3. `MEMORY.md` ve `PROGRESS.md`
4. İlgili oyun kitabı (`playbooks/growth-and-packaging.md`, `playbooks/competitor-remake.md`, `playbooks/tts-and-music-stack.md`)
5. Hedef kanalın profil dosyası (`channels/<kanal>/CHANNEL.md`)
6. Çekirdek yönlendirici (`core/skills/studio-router/SKILL.md`)

**Onay Kapısı (Yönetmen Kilidi):**
- Kullanıcı onaylamadan final render alma, YouTube'a `public` yayın yapma, `git push` atma veya ağır AI model/paket indirmesi başlatma.
- YouTube API yüklemeleri istisnasız **`private`** taslak olarak yapılır.

---

## §1. Değişmez Kanal ve Format Kuralları

1. **Shorts / Uzun Video Kanal Ayrımı (Kesin Yasak):**
   - Hiçbir kanala hem Shorts hem uzun video yüklenmez.
   - Her kanal `channels/<kanal>/CHANNEL.md` içinde `long-only` veya `shorts-only` olarak kilitlenir.
   - Shorts süresi en fazla **59 saniye** (40–58 sn ideal) olmalıdır.
2. **Rakip Kopya & Özgünlük Kilidi:**
   - Rakip video fikirleri ve metin omurgaları analiz edilir ancak **kelimesi kelimesine kopyalama yasaktır**.
   - İsimler, yerler, mekanlar ve cümle yapıları mutlaka değiştirilir; yalnızca kanıtlanmış ana tema, merak boşluğu ve anlatım gücü korunur.
   - Küçük resimde (thumbnail) en çok izlenen rakibe yapısal benzerlik korunurken **en az 2 belirgin öge/renk/kompozisyon farkı** zorunludur.
3. **Thumbnail + Başlık Tek Birim Kuralı:**
   - Küçük resimde en fazla **3–4 kelime**, zıt/kontrastlı renkler ve merak boşluğu kullanılır; kalabalık yazı/logo eklenmez.
   - Başlıktaki kelimeler thumbnail metninde tekrarlanmaz; tüm sözlü videolarda `python3 core/scripts/yt_title_lint.py` çalıştırılır.
4. **Açıklama & Tek Link Kuralı:**
   - Video açıklamasında **yalnızca tek bir link** (en yüksek dönüştürücü / VSL videosunun linki) bulunur.
   - Instagram, TikTok, X vb. tüm dış sosyal medya linkleri video açıklamasından yasaktır (sadece kanal hakkında/biyografi alanında yer alır).
   - Açıklamanın ilk 2 satırı anahtar kelime yoğunluklu, videoyu net özetleyen altın SEO bloğudur.
5. **Bilgi Doğruluğu & Hukuki Uyarı Kapısı:**
   - Hiçbir nişte uydurma veya yanlış bilgi yayınlanmaz (YouTube gri alan / güven kaybı riski).
   - `#03 Finans` videolarında yatırım tavsiyesi olmadığı (yalnızca temel finans eğitimi) yazılı ve sözlü belirtilir.

---

## §2. Yayın ve Algoritma Hijyeni

1. **Kanal Isıtma:** Yeni açılmış mail/kanala ilk gün video yüklenmez. Profil, banner, anahtar kelimeler, yükleme varsayılanları ve SEO ağırlıklı Hakkında metni tamamlandıktan sonra **1–2 gün** beklenir; hesap doğal izleme/beğeni/yorum ile ısıtılır.
2. **Gizli Yükleme & Çeyrek Saat Zamanlaması:** Video önce **`private`** yüklenir, 1–2 saat bekletilir; ardından izleyici yoğun saatinden **~1 saat önce** ve tam saat yerine **çeyrek geçe (`:15` veya `:45`)** yayına alınır.
3. **Yayın Sonrası Yasaklar:**
   - Kendi videonu yayınlandıktan hemen sonra açıp 5–10 saniye izleyip çıkmak **yasaktır**.
   - İlk **2–3 hafta** dolmadan başlık ve küçük resim değiştirilmez.
   - İzlenmiyor diye video silinmez (gerekmedikçe), kesinlikle izlenme/abone satın alınmaz.
   - Videoyu sonuna kadar izlemeyecek eş/dost gruplarına link dağıtılmaz.
4. **Çoklu Platform Odağı:** Yeni/küçük kanallarda aynı anda her platforma video basılmaz; ana odak YouTube + sadece trafik çekmek için Instagram hikâyesidir.

---

## §3. Teknik Üretim ve Kalite Kapıları

1. **Yüzsüz & Lokal Üretim Önceliği:** Varsayılan yığın %100 ücretsiz/yerel araçlardır (`playbooks/tts-and-music-stack.md`). Suno/Udio/ElevenLabs ücretsiz planları ticari telif riski nedeniyle üretimde kullanılmaz.
2. **Sözlü Videolar (`spoken-essay`):**
   - Senaryo kancası `python3 core/scripts/yt_hookscore.py` ile puanlanır.
   - Kesim sırası `core/AGENTS.md` kuralına uyar: önce tekrar/flub (`ffmpeg select`), sonra sessizlik; altyazı en sonda işlenir.
   - Çıktı `python3 core/scripts/qc_gate.py <mp4> --profile youtube` (`-14 LUFS`, true peak `<= -1.0 dBTP`) ve `python3 core/scripts/caption_and_chapters.py` (`00:00` ile başlayan >=3 bölüm, her biri >=10 sn) kapısından geçer.
3. **Sözsüz Meditasyon / Ambiyans Videoları (`silent-meditation-loop`, 1–8 saat):**
   - Sessizlik kesimi **uygulanmaz**; konuşma altyazısı **eklenmez**.
   - Kısa 3–5 dakikalık telifsiz/yerel ambient müzik ve görsel katmanı `python3 scripts/meditation_loop.py` ile dikişsiz uzatılır (hedef `-18 LUFS`, tavan `-1.0 dBTP`).
4. **Çekirdek Bağlılığı:** Çekirdek skill/script güncellemeleri `core/` üzerinden alınır (`scripts/sync_core.sh` veya `scripts/sync_core.ps1`); `core/` klasörü içinde doğrudan dosya düzenlenmez (değişiklik gerekiyorsa `CONTENTY` reposunda yapılır).
