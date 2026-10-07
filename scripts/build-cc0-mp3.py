#!/usr/bin/env python3
from pathlib import Path
import subprocess, urllib.request, zipfile, shutil

ROOT=Path(__file__).resolve().parents[1]
RAW=ROOT/"build"/"raw"
OUT=ROOT/"build"/"mp3"
RAW.mkdir(parents=True, exist_ok=True)
OUT.mkdir(parents=True, exist_ok=True)

# Direct files/pages with explicit CC0 and MP3 availability.
FILES = {
    "hit/skill_hit.mp3":"https://opengameart.org/sites/default/files/skill_hit.mp3",
    "hit/attack_hit.mp3":"https://opengameart.org/sites/default/files/attack_hit.mp3",
    "hit/attack_hit_1.mp3":"https://opengameart.org/sites/default/files/attack_hit_1.mp3",
    "hit/playerhit.mp3":"https://opengameart.org/sites/default/files/playerhit.mp3",
    "hit/hurt_01.mp3":"https://opengameart.org/sites/default/files/hurt_01.mp3",
    "hit/hurt_02.mp3":"https://opengameart.org/sites/default/files/hurt_02.mp3",
    "hit/hurt_03.mp3":"https://opengameart.org/sites/default/files/hurt_03.mp3",
    "hit/hurt_04.mp3":"https://opengameart.org/sites/default/files/hurt_04.mp3",
    "hit/hurt_05.mp3":"https://opengameart.org/sites/default/files/hurt_05.mp3",
    "hit/hurt_06.mp3":"https://opengameart.org/sites/default/files/hurt_06.mp3",
    "death/slimy_monster_or_murderd_sound.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound.mp3",
    "death/slimy_monster_or_murderd_sound_1.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_1.mp3",
    "death/slimy_monster_or_murderd_sound_2.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_2.mp3",
    "death/slimy_monster_or_murderd_sound_3.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_3.mp3",
    "death/slimy_monster_or_murderd_sound_4.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_4.mp3",
    "death/slimy_monster_or_murderd_sound_5.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_5.mp3",
    "death/slimy_monster_or_murderd_sound_6.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_6.mp3",
    "death/slimy_monster_or_murderd_sound_7.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_7.mp3",
    "death/slimy_monster_or_murderd_sound_8.mp3":"https://opengameart.org/sites/default/files/slimy_monster_or_murderd_sound_8.mp3",
    "death/high_pitch_scream_gverb.mp3":"https://opengameart.org/sites/default/files/high_pitch_scream_gverb.mp3",
    "death/high_pitch_scream.mp3":"https://opengameart.org/sites/default/files/high_pitch_scream.mp3",
    "funny/littlegrunts.mp3":"https://opengameart.org/sites/default/files/littlegrunts.mp3",
    "funny/accordion_squeeze.mp3":"https://opengameart.org/sites/default/files/accordion_squeeze.mp3",
    "magic/fantasy_magic_button_1.mp3":"https://opengameart.org/sites/default/files/fantasy_magic_button_1.mp3",
    "magic/fire_sound_effect.mp3":"https://opengameart.org/sites/default/files/fire_sound_effect.mp3",
}

def fetch(rel, url):
    dest=OUT/rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    if dest.exists():
        return
    print("GET", url)
    urllib.request.urlretrieve(url, dest)

for rel,url in FILES.items():
    fetch(rel,url)

# Pack-level CC0 sources: download and convert every audio file to MP3.
PACKS = {
    "zombie_cartoon/creatures":"https://opengameart.org/sites/default/files/80-CC0-creature-SFX.zip",
    "rpg/80-rpg":"https://opengameart.org/sites/default/files/80-CC0-RPG-SFX.zip",
    "rpg/8bit":"https://opengameart.org/sites/default/files/8-bit%20Sound%20Effects%20Pack%20001.zip",
}
for name,url in PACKS.items():
    z=RAW/(name.replace("/","_")+".zip")
    if not z.exists():
        print("GET",url)
        urllib.request.urlretrieve(url,z)
    d=RAW/name
    if not d.exists():
        d.mkdir(parents=True)
        with zipfile.ZipFile(z) as f:
            f.extractall(d)
    for src in d.rglob("*"):
        if src.suffix.lower() not in {".wav",".ogg",".flac",".mp3"}:
            continue
        rel=src.relative_to(d)
        dest=OUT/name/rel.with_suffix(".mp3")
        dest.parent.mkdir(parents=True,exist_ok=True)
        if dest.exists():
            continue
        subprocess.run(["ffmpeg","-y","-i",str(src),"-codec:a","libmp3lame","-q:a","3",str(dest)],
                       check=True,stdout=subprocess.DEVNULL,stderr=subprocess.DEVNULL)

print("Done:", len(list(OUT.rglob("*.mp3"))), "MP3 files")
