$ErrorActionPreference = "Stop"
$root = Split-Path -Parent $PSScriptRoot
$assets = Join-Path $root "assets"
New-Item -ItemType Directory -Force -Path $assets | Out-Null
$tmp = Join-Path $env:TEMP "YandexGameSFX"
if (Test-Path $tmp) { Remove-Item -Recurse -Force $tmp }
New-Item -ItemType Directory -Force -Path $tmp | Out-Null

git clone --depth 1 https://github.com/Mcamento8/open-game-sfx-index.git "$tmp/open-game-sfx-index"
git clone --depth 1 https://github.com/lavenderdotpet/CC0-Public-Domain-Sounds.git "$tmp/cc0-public-domain-sounds"

Remove-Item -Recurse -Force (Join-Path $assets "open-game-sfx-index") -ErrorAction SilentlyContinue
Remove-Item -Recurse -Force (Join-Path $assets "cc0-public-domain-sounds") -ErrorAction SilentlyContinue
Copy-Item "$tmp/open-game-sfx-index" (Join-Path $assets "open-game-sfx-index") -Recurse
Copy-Item "$tmp/cc0-public-domain-sounds" (Join-Path $assets "cc0-public-domain-sounds") -Recurse

Write-Host "SFX sources downloaded to assets/"
