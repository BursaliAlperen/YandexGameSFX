#!/usr/bin/env python3
import shutil, sys
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
SRC=ROOT/"assets"
OUT=ROOT/"categorized"
CATS=["ui","click","hit","impact","magic","attack","sword","death","monster","zombie","explosion","coin","pickup","whoosh","footstep","laser","powerup","levelup","animal","ambient","misc"]
RULES={"zombie":["zombie","undead","groan","moan","gore"],"monster":["monster","creature","growl","roar","beast","alien"],"death":["death","die","dead","gameover","defeat","kill","scream"],"explosion":["explosion","explode","blast","bomb","boom"],"magic":["magic","spell","cast","curse","fire","ice","earth","arcane","witch"],"sword":["sword","blade","slash","clash","saber","knife"],"hit":["hit","punch","thwack","smack","hurt","damage"],"impact":["impact","crash","slam","thud"],"attack":["attack","strike","shoot","shot","weapon"],"click":["click","button","press","switch","toggle"],"ui":["ui","interface","menu","select","confirm","cancel","hover","error","notification"],"coin":["coin","money","cash","gold","gem"],"pickup":["pickup","pick","collect","item","chest","bonus"],"whoosh":["whoosh","swish","swoosh","swing","wind"],"footstep":["footstep","step","walk","run"],"laser":["laser","phaser","beam","zap","ray"],"powerup":["powerup","power-up","power","bonus","upgrade"],"levelup":["levelup","level-up","level up","achievement"],"animal":["animal","dog","cat","bird","horse","rat","frog"],"ambient":["ambient","wind","rain","water","fire","nature"]}
def classify(name):
    s=name.lower().replace("_"," ").replace("-"," ")
    scores={c:sum(k in s for k in keys) for c,keys in RULES.items()}
    best=max(scores,key=scores.get)
    return best if scores[best] else "misc"
if not SRC.exists():
    print("Source not found. Run scripts/download-sfx first.", file=sys.stderr); sys.exit(1)
for c in CATS: (OUT/c).mkdir(parents=True,exist_ok=True)
count=0
for p in SRC.rglob("*"):
    if not p.is_file() or p.suffix.lower() not in {".ogg",".wav",".flac",".mp3"}: continue
    cat=classify(p.stem); target=OUT/cat/p.name
    if target.exists(): target=OUT/cat/(p.stem+"_"+str(abs(hash(str(p))))+p.suffix)
    shutil.copy2(p,target); count+=1
print(f"Categorized {count} audio files into {OUT}")
