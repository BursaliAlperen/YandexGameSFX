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
