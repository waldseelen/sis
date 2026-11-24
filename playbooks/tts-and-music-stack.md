# %100 Ücretsiz ve Yerel Seslendirme, Müzik ve Görsel Motor Yığını

Bu doküman **Windows 11 ince kasa NPU'lu ASUS Vivobook** hedef donanımına göre tasarlanmıştır.
> **Kural:** Yeni laptop hazır olana kadar hiçbir ağır model veya pip paketi otomatik indirilmez; burada yalnızca kullanılacak araç kararları ve iki katmanlı donanım yönlendirmesi kilitlenir.

---

## 1. Seslendirme (TTS) — Robotik Olmayan Ücretsiz İnsan Sesi

> [!CAUTION] Yasaklı Ücretli / Freemium Araçlar (ElevenLabs Kullanılamaz)
> Yalnızca LLM/AI ajan sağlayıcısı dışında hiçbir araca bütçe ayrılmaz ve **ElevenLabs kullanılamaz** (ücretsiz planı ticari YouTube monetizasyon hakkı vermez, ücretli abonelik de bütçe dışıdır). Tüm kanallarda yalnızca aşağıdaki %100 ücretsiz açık kaynak yığın kullanılır.

### Katman 1 — CPU / ONNX (İnce Kasa Laptopta Kesin Çalışır — Varsayılan)
1. **Kokoro-82M (`kokoro-onnx` — Apache-2.0):**
   - **Neden 1 numara:** İngilizce doğallığı çok yüksek, robotik değil, GPU gerektirmeden CPU'da bile gerçek zamanlıdan hızlı çalışır, ticari kullanımı tamamen serbesttir.
   - **Kullanılan kanallar:** `#06 Stoic Discipline` (İngilizce), `#01 Ehliyet Pass Test`, `#02 Magnificent Empress`, `#05 Meditasyon` (varsa kısa giriş).
   - **Üretim sözleşmesi:** `core/skills/audio-and-roughcut/SKILL.md` içindeki `manifest.json` süre sözleşmesiyle sahne bazlı senkronlanır.
2. **Edge TTS (`edge-tts` Python paketi):**
   - **Rolü:** Türkçe kanallar (`#03 Finans`, `#04 Sağlık`, `#08`–`#12`) için sıfır GPU yüküyle hızlı neural seslendirme (Kokoro henüz Türkçe desteklemediği için).

### Katman 2 — GPU / Opsiyonel İleri Ses Klonlama (VRAM Yeterliyse veya Ücretsiz Colab)
3. **Chatterbox (Resemble AI — MIT)** & **Fish Speech (MIT):**
   - Kısa bir ses örneğinden zero-shot ses klonlama ve vurgu/nefes (`[sigh]`, duraksama) kontrolü sunar.
   - İnce kasa laptopta GPU VRAM'i sınırlıysa ücretsiz Google Colab üzerinde bölüm sesleri üretilip WAV olarak yerel kurguya alınır.

---

## 2. Müzik ve Ambiyans AI — Sözsüz Stoic & Meditasyon

> [!CAUTION] Suno & Udio Kullanılamaz
> Yalnızca LLM/AI ajan sağlayıcısı dışında ücretli abonelik açılmaz; **Suno ve Udio (ücretli veya ücretsiz) kullanılamaz** (ücretsiz planlarda ticari hak platforma aittir ve YouTube Content ID/telif riski doğurur).

### Katman 1 — Sıfır Telif + Düşük Donanım Yükü (Varsayılan)
1. **YouTube Audio Library + Pixabay / Freesound `CC0` Stem'leri:**
   - Derin ambient pad, yağmur, şömine, rüzgar ve minimal piyano katmanları yerel olarak birleştirilir (`04-audio/sources.json` lisans kaydıyla).
2. **8 Saatlik Dikişsiz Döngü Tekniği (`scripts/meditation_loop.py`):**
   - Hiçbir AI tek seferde 8 saat müzik üretmez. 3–5 dakikalık temiz bir stem üretilir/seçilir; `ffmpeg` `acrossfade` filtresiyle sıfır tıkırtıyla 1–8 saate uzatılır (`-18 LUFS`, `-1.0 dBTP`).

### Katman 2 — Yerel Açık Kaynak Müzik Üretimi (GPU veya Colab)
3. **Stable Audio Open 1.0:** Sözsüz ambient, drone, sinematik atmosfer ve ses tasarımı için en temiz açık kaynak modellerden biri.
4. **MusicGen (Meta AudioCraft):** Kısa (30 sn–3 dk) tematik arka plan döngüleri için.
5. **ACE-Step:** Daha uzun enstrümantal parçalar üretmek için açık kaynak alternatif.

---

## 3. Yüzsüz Görsel & Kurgu Motorları (`core/` Üzerinden)

Her kanal formatına göre `core/skills/faceless-and-shorts/SKILL.md` seçicisi uygulanır:
- **Basit/Hızlı Bilgi & Alıntı (`#01`, `#03`, `#04`, `#06` Mod A):** `PIL + PNG + FFmpeg` (Ken Burns `--zoom in`, sıfır Node yükü) veya `HyperFrames` (HTML/CSS/GSAP).
- **Sözsüz Meditasyon (`#05`, `#06` Mod B):** Tek yüksek çözünürlüklü statik/hafif nefes alan görsel + `scripts/meditation_loop.py`.
- **Hikâye / Çizgi Film / Masal (`#08`–`#12`):** `core/skills/video-prompt-builder/SKILL.md` ile sahne akışı + açık kaynak yerel ComfyUI (`FUTURE.md` bölüm 6) veya ücretsiz/CC0 illüstrasyon katmanları.
- **Altyazı & Zaman Damgası:** Yerel `faster-whisper` (`core/scripts/transcribe.py`, `int8` CPU dostu) + `core/scripts/caption_and_chapters.py`.
