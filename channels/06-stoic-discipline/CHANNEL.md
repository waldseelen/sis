# Kanal #06 — Stoic Discipline ★ ÖNCELİK 1

- **Durum:** `priority-1` (ilk inşa edilecek ve yayınlanacak ana kanal)
- **Format Kilidi:** `long-only` (Shorts atılmaz; ayrı kanal kuralı)
- **Dil & Hedef Kitle:** Global İngilizce (`en`) + çok dilli `.srt` (`es`, `de`, `tr`) + otomatik dublaj aktif
- **Niş Harmanlama:** **Stoacılık + Disiplin/Alışkanlık/İstikrar/Özsaygı/Psikoloji + Sözsüz Stoic Meditasyon** (üçlü benzer kitleyi tek kanalda toplama stratejisi)
- **Üretim Modu:** Çift Modlu (`spoken-essay` + `silent-meditation-loop`)
- **Ses Motoru:** `kokoro-82m` (Tier 1 CPU/ONNX — birincil) / `chatterbox` (Tier 2 GPU/Colab ses klonlama)
- **Müzik Kaynağı:** `cc0-stems` / `yt-audio-library` / Tier 2 `stable-audio` & `ace-step`
- **Hedef Loudness:** Mod A `-14 LUFS` | Mod B `-18 LUFS` (`<= -1.0 dBTP`)

---

## 1. Referans Kanallar & Outlier Kıyasları

| Referans | Ölçek / Kanıt | Çıkarılacak Ders |
| :--- | :--- | :--- |
| [Ana Referans Video 1 (`8vOojviWwRk`)](https://youtu.be/8vOojviWwRk) | ~9M izlenme, 1.48M abone, 5 yıllık kanal | Ana anlatım omurgası, tonlama, stoik tempo, başlık/kapak kontrastı. |
| [Referans Video 2 (`s3vdNNBX98w`)](https://youtu.be/s3vdNNBX98w) | 25M max izlenme, 22K abone, 3 yıllık kanal | **Altın outlier kanıtı:** Düşük aboneye rağmen devasa izlenme → fikir + kanca + paketleme gücü. |
| [Meditasyon Referans Kanal (`@meditations.acepe.`)](https://youtube.com/@meditations.acepe.) | 135K abone, 2.5M max izlenme, 3 yıllık kanal | Sıfır sahne/edit/animasyon/seslendirme/yazı ile başarı; üyelere özel 8 saatlik uzun videolar. |

---

## 2. Çift Modlu Üretim Boru Hattı

### Mod A — Sözlü Stoic Essay / Disiplin Videosu (`spoken-essay`)
1. **Outlier Seçimi:** Yukarıdaki referanslardan veya son 1 yılın yüksek izlenen düşük aboneli rakiplerinden 1 konu seç (`playbooks/competitor-remake.md`).
2. **Özgün Yeniden Yazım:** Rakibin transkriptini `yt-dlp` ile al; isimleri, yerleri, örnekleri ve tüm cümleleri değiştir; samimi, otoriter, film sonu gibi biten HPC akışı kur.
3. **Kanca & Kapak Kontrolü:**
   - `python3 core/scripts/yt_hookscore.py --hook "<ilk cumle>" --json`
   - `python3 core/scripts/yt_title_lint.py --title "<baslik>" --thumb "<3-4 kelime>" --json`
   - Kapakta rakibe göre **en az 2 öge/renk farkı** (koyu taş/altın/zümrüt tonları, mermer büst/yalnız silüet, merak boşluğu).
4. **Ses & Görsel:**
   - `Kokoro-82M` ile sakin, tok İngilizce seslendirme (`manifest.json` süre haritasıyla).
   - Arkada çok hafif ambient drone/yağmur (`-15 dB` ducking), koyu minimalist görseller / yavaş Ken Burns / alıntı kartları (`PIL` veya `HyperFrames`).
5. **Çıkış & Yayın:** Harici çok dilli `.srt` + gerçek `chapters` + `core/scripts/qc_gate.py --profile youtube` → `private` yükleme → `:15`/`:45` yayın.

### Mod B — Sözsüz Stoic Meditasyon (`silent-meditation-loop`, 1–8 saat)
1. **Neden Kolay & Hızlı:** Görüntü değişimi yok, sahne yok, ağır edit yok, animasyon yok, seslendirme yok, yazı/metin yok.
2. **Üretim:**
   - 1 adet loş, sinematik Stoic görsel (16:9, 1920x1080 veya 4K) + 1 adet 3–5 dakikalık karanlık ambient/piyano/drone stem.
   - Komut:
     ```bash
     python3 scripts/meditation_loop.py \
       --audio channels/06-stoic-discipline/episodes/<ep>/04-audio/stem.wav \
       --image channels/06-stoic-discipline/episodes/<ep>/03-graphics/bg.png \
       --hours 3 \
       --output channels/06-stoic-discipline/episodes/<ep>/05-exports/final_3h.mp4
     ```
   - Üyelere özel 8 saatlik versiyonda `--hours 8`.
3. **Yükleme:** `private` taslak → izleyici zirvesinden ~1 saat önce `:15`/`:45` yayına al; açıklamada tek VSL linki.
