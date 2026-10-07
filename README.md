# YandexGameSFX

CC0/public-domain game SFX bootstrap library for Yandex Games.

## Quick start

Windows:
```powershell
powershell -ExecutionPolicy Bypass -File .\scripts\download-sfx.ps1
```

Linux/macOS:
```bash
bash scripts/download-sfx.sh
```

The downloader pulls verified CC0/public-domain source collections into `assets/`. We intentionally keep large binary packs out of Git history.

## Categories

Planned game-use categories: ui, click, hit, impact, magic, attack, sword, death, monster, zombie, explosion, coin, pickup, whoosh, misc.

## Important

Always retain SOURCES.md when redistributing downloaded audio and re-check upstream licenses before adding new sources.

## Build the larger CC0 pool

1. Run `scripts/download-sfx.ps1` (or `.sh`).
2. Run `python scripts/download-extra-cc0.py` for additional verified CC0 OpenGameArt packs.
3. Run `python scripts/categorize_sfx.py` to classify downloaded audio automatically.

The extra pool contains overlapping packs intentionally; deduplicate by SHA-256 before shipping a final game bundle. The primary Open Game SFX Index currently catalogs 1,451 CC0/public-domain effects. citeturn0search1
