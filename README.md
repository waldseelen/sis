# sis — Çok Kanallı YouTube Üretim Stüdyosu

`waldseelen/CONTENTY` çekirdek motoru (`core/` submodule) üzerine kurulu, **12 kanallı**, %100 ücretsiz/yerel odaklı tam otonom YouTube üretim stüdyosu.

> **İçerik üreticisiysen (teknik detaylarla uğraşmak istemiyorsan):** Doğrudan **`BASLA.md`** dosyasını aç — tüm hazır istek örnekleri orada. Ajan tüm teknik işleri arka planda kendisi halleder.

---

## Hızlı Başlangıç (Windows 11 / Linux / macOS)

### 1. Repoyu Çekirdekle Birlikte Klonla
```bash
git clone --recurse-submodules https://github.com/waldseelen/sis.git
cd sis
```

### 2. Ajan Ortamını Bağla (Model İndirmez)
- **Windows (PowerShell):**
  ```powershell
  .\scripts\setup.ps1 -Target all
  ```
- **Linux / macOS:**
  ```bash
  ./scripts/setup.sh all
  ```
Desteklenen ajanlar: **Antigravity**, **Claude Code**, **OpenCode**.

### 3. Çekirdek (`CONTENTY`) Güncellemelerini Al
`CONTENTY` üzerinde yeni skill, plugin, hook veya script güncellendiğinde:
- Windows: `.\scripts\sync_core.ps1`
- Linux/macOS: `./scripts/sync_core.sh`

---

## Kanal Envanteri (`channels/`)

| # | Klasör | Niş / Odak | Öncelik / Durum |
| :---: | :--- | :--- | :--- |
| 01 | `channels/01-ehliyet-pass-test` | Ehliyet Yazılı Sınavları (USA/UK/CA yaşlı sürücüler) | Aktif |
| 02 | `channels/02-magnificent-empress` | Dişilik, ilişki tavsiyeleri, feminen müzik | Açıldı (henüz yükleme yok) |
| 03 | `channels/03-finans` | Para yönetimi, yatırım, yüksek RPM finans eğitimi | Planlı |
| 04 | `channels/04-saglik` | Bilimsel sağlık bilgileri | Planlı |
| 05 | `channels/05-meditasyon` | Rahatlama, uyku, 1–8 saat sözsüz meditasyon | Planlı |
| **06** | **`channels/06-stoic-discipline`** | **Stoacılık, disiplin, alışkanlık, sözsüz Stoic meditasyon** | **★ ÖNCELİK 1** |
| 07 | `channels/07-bagimsiz-muzik` | Bağımsız çok türden müzik | Planlı |
| 08 | `channels/08-ibretlik-hikayeler` | İbretlik yetişkin hikâyeleri (Sırlar Dünyası tarzı) | Planlı |
| 09 | `channels/09-cizgi-film` | Çizgi film içerikleri | Planlı |
| 10 | `channels/10-masal-anlatimi` | Masal anlatımı | Planlı |
| 11 | `channels/11-hikaye-anlatimi` | Hikâye anlatımı | Planlı |
| 12 | `channels/12-sesli-kitap` | Sesli kitap | Planlı |

---

## Temel Belgeler
- Kurallar ve kapılar: `CLAUDE.md`
- Mimari ve çekirdek bağı: `ARCHITECTURE.md`
- Teknik sözleşmeler: `SPEC.md`
- Strateji & paketleme rehberi: `playbooks/growth-and-packaging.md`
- Rakip analiz & yeniden yazım: `playbooks/competitor-remake.md`
- Ücretsiz yerel TTS & müzik yığını: `playbooks/tts-and-music-stack.md`
