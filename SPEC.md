# SPEC.md — `sis` Üretim Sözleşmesi ve Kanal Şemaları

## 1. Kanal Profili Sözleşmesi (`channels/<slug>/CHANNEL.md`)

Her kanal klasörü şu zorunlu alanları tanımlayan bir `CHANNEL.md` ve ham/çıktı medyanın git dışında tutulacağı `episodes/` klasörünü içerir:

| Alan | Değerler / Format | Açıklama |
| :--- | :--- | :--- |
| **Kanal ID & Durum** | `01`..`12` / `active \| pre-launch \| planned` | Mevcut açılış ve yayın durumu |
| **Format Kilidi** | `long-only \| shorts-only` | Aynı kanala karışık format yasağı |
| **Dil & Hedef Pazar** | `en`, `tr`, `en+multilang-srt` | Ana ses ve altyazı hedefi |
| **Üretim Modu** | `spoken-essay \| silent-meditation-loop \| music-visual \| storytelling` | Kullanılacak boru hattı |
| **Ses Motoru** | `kokoro-82m \| edge-tts \| chatterbox \| none` | Varsayılan TTS katmanı |
| **Müzik / Ses Kaynağı** | `yt-audio-library \| cc0-stems \| stable-audio \| ace-step \| none` | Telifsiz müzik kaynağı |
| **Hedef Loudness** | `-14 LUFS` (konuşmalı) / `-18 LUFS` (meditasyon) | True peak tavanı `<= -1.0 dBTP` |

---

## 2. Öncelik #06 (`06-stoic-discipline`) Çift Modlu Üretim Sözleşmesi

### Mod A: Sözlü Stoic / Disiplin Videosu (`spoken-essay`)
1. **Araştırma:** `yt-dlp` ile outlier rakibin meta verisi ve transkripti çekilir (`playbooks/competitor-remake.md`).
2. **Özgünleştirme & Senaryo:** Konu omurgası korunur; cümleler, isimler, örnekler ve mekanlar tamamen yeniden yazılır. `4 parçalı` veya `HPC` (Hook → Open Loops → Ödül → Sonraki Video Köprüsü) yapısı uygulanır.
3. **Paketleme Kapısı:** `yt_hookscore.py` + `yt_title_lint.py` (başlık ve kapakta sıfır ortak kelime, kapakta rakibe göre >= 2 öge/renk farkı).
4. **Seslendirme:** İngilizce için `Kokoro-82M (ONNX)` (Tier 1) veya GPU/Colab'da `Chatterbox` (Tier 2).
5. **Görsel & Kurgu:** Koyu minimalist arka plan + alıntı/bölüm kartları (`PIL`/`HyperFrames`) + ince hareket; kesim sonrası harici çok dilli `.srt` (`en`, `es`, `de`, `tr`).
6. **Kalite & Yükleme:** `core/scripts/qc_gate.py --profile youtube` + `core/scripts/caption_and_chapters.py` sonrası `private` yükleme ve `:15`/`:45` yayına alma.

### Mod B: Sözsüz Stoic Meditasyon / Uyku (`silent-meditation-loop`, 1–8 saat)
1. **Girdi:** 1 adet statik 16:9 görsel (1920x1080 veya 3840x2160) veya kısa dikişsiz video döngüsü + 1 adet 3–5 dakikalık telifsiz ambient/drone müzik stem'i.
2. **Sözsüz Kural:** Konuşma, TTS, altyazı ve agresif görsel kesim **yoktur**.
3. **Üretim (`scripts/meditation_loop.py`):**
   - Ses dosyası `ffmpeg` `acrossfade` filtresiyle dikişsiz şekilde hedef süreye (örn. `3600`–`28800` saniye) uzatılır ve `-18 LUFS` / `-1.0 dBTP` seviyesine normalize edilir.
   - Görsel/video düşük CPU maliyetli sabit FPS (`24` veya `1`–`2` fps statik görsel için) ve keyframe dostu ayarlarla sesle birleştirilir (`-shortest`).
4. **Doğrulama:** `ffprobe` ile hedef süre (`±2 sn`) ve A/V akış bütünlüğü doğrulanır.

---

## 3. `scripts/meditation_loop.py` CLI Sözleşmesi

```text
python3 scripts/meditation_loop.py \
  --audio <stem.wav|mp3> \
  --image <bg.png> | --video <loop.mp4> \
  --hours <1..8 | --seconds N> \
  --output <out.mp4> \
  [--crossfade 4.0] [--lufs -18] [--width 1920 --height 1080 --fps 24] \
  [--dry-run]
```
- `--dry-run`: FFmpeg çalıştırmadan hesaplanan tekrar sayısını, `filter_complex` grafiğini ve tam komutu doğrular.
- Çıktı dosyasının üst klasörü yoksa oluşturur; mevcut kaynak dosyasının üzerine asla yazmaz.

---

## 4. Kurulum, Senkronizasyon ve Çoklu Kanal Durum Sözleşmesi

- `setup.sh` / `setup.ps1` **idempotent**tir; model veya ağır pip paketi otomatik indirmez (yalnızca ajan bağlantılarını ve dizin kontrollerini yapar).
- `sync_core.sh` / `sync_core.ps1`, `core/` alt modülünü `origin/main` ucuna çeker (`git submodule update --remote --merge core`).
- `python3 scripts/studio_status.py [--json]`: 12 kanalın `CHANNEL.md` meta verilerini ve bölüm sayılarını okuyarak ajanın operatöre sade Türkçe durum özeti sunmasını sağlar.
- **Operatör Deneyimi Sözleşmesi:** Ajan geliştirici dili kullanmaz; tüm teknik adımları, dosya/klasör açmayı ve yerel kurulumları arka planda otonom yürütür (`CLAUDE.md` §1 ve `.agents/rules/sis-producer.md`).
