#!/usr/bin/env python3
import io, zipfile, urllib.request, shutil
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
OUT=ROOT/"assets"/"extra-cc0"
OUT.mkdir(parents=True,exist_ok=True)

PACKS=[
("100-cc0-sfx","https://opengameart.org/sites/default/files/100-CC0-SFX.zip"),
("100-cc0-sfx-2","https://opengameart.org/sites/default/files/sfx_100_v2.zip"),
("80-cc0-rpg","https://opengameart.org/sites/default/files/80-CC0-RPG-SFX.zip"),
("80-cc0-creature-2","https://opengameart.org/sites/default/files/80-CC0-creature-sfx-2.zip"),
("75-breaking-falling-hit","https://opengameart.org/sites/default/files/sfx_breaking_and_falling.zip"),
("40-water-splash-slime","https://opengameart.org/sites/default/files/water-splash-slime-sfx.zip"),
("50-retro-synth","https://opengameart.org/sites/default/files/50-CC0-retro-synth-SFX.zip"),
("50-sci-fi","https://opengameart.org/sites/default/files/sci-fi-sfx.zip"),
("sound-effects-pack-2","https://opengameart.org/sites/default/files/Sound%20effects%20Pack%202.zip"),
("mini-pack-1.5","https://opengameart.org/sites/default/files/Sound%20effects%20Mini%20Pack1.5.zip"),
("20-sword-attacks","https://opengameart.org/sites/default/files/sword_-_starninjas.zip"),
("20-sword-clashes","https://opengameart.org/sites/default/files/sword_clash_-_starninjas.zip"),
("random-sfx","https://opengameart.org/sites/default/files/SFX.zip"),
("deep-bone-breaks","https://opengameart.org/sites/default/files/deep_breaks.zip"),
("bub-block","https://opengameart.org/sites/default/files/bubsfx.zip"),
("scrapes","https://opengameart.org/sites/default/files/scrapes.zip"),
]

for name,url in PACKS:
    dest=OUT/name
    if dest.exists(): shutil.rmtree(dest)
    dest.mkdir(parents=True)
    print("Downloading",name)
    data=urllib.request.urlopen(url,timeout=60).read()
    try:
        with zipfile.ZipFile(io.BytesIO(data)) as z:
            z.extractall(dest)
    except zipfile.BadZipFile:
        (dest/"DOWNLOAD_FAILED.txt").write_text("Could not read ZIP: "+url,encoding="utf-8")
print("Finished. Review SOURCES.md and duplicates before shipping.")
