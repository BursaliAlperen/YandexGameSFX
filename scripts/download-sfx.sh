#!/usr/bin/env bash
set -euo pipefail
ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")/.." && pwd)"
ASSETS="$ROOT/assets"
mkdir -p "$ASSETS"
TMP="$(mktemp -d)"
trap 'rm -rf "$TMP"' EXIT

git clone --depth 1 https://github.com/Mcamento8/open-game-sfx-index.git "$TMP/open-game-sfx-index"
git clone --depth 1 https://github.com/lavenderdotpet/CC0-Public-Domain-Sounds.git "$TMP/cc0-public-domain-sounds"

rm -rf "$ASSETS/open-game-sfx-index" "$ASSETS/cc0-public-domain-sounds"
cp -R "$TMP/open-game-sfx-index" "$ASSETS/open-game-sfx-index"
cp -R "$TMP/cc0-public-domain-sounds" "$ASSETS/cc0-public-domain-sounds"

echo "SFX sources downloaded to assets/"
