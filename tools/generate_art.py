#!/usr/bin/env python3
"""Schatten-Arsenal 0.8: high contrast pixel-art armor, equipment, and boss trophies.
Generated deterministically so GitHub Actions can build the same JAR each run.
"""
from pathlib import Path
import json, random
from PIL import Image, ImageDraw

ROOT=Path("src/main/resources/assets/schattenarsenal")
TEXTURES=ROOT/"textures"
VOID=(10,9,20,255)
BLACK=(17,16,30,255)
STEEL=(37,34,57,255)
METAL=(53,49,78,255)
EDGE=(81,74,114,255)
PURPLE=(112,36,200,255)
ROYAL=(150,49,229,255)
LUMEN=(208,91,255,255)
GLINT=(249,182,255,255)
PINK=(249,112,221,255)
SHADOW=(8,5,14,255)

def pixel(im,x,y,c):
    if 0<=x<im.width and 0<=y<im.height: im.putpixel((x,y),c)

def save(im,relative,scale=2):
    path=TEXTURES/relative
    path.parent.mkdir(parents=True,exist_ok=True)
    if scale!=1: im=im.resize((im.width*scale,im.height*scale),Image.Resampling.NEAREST)
    im.save(path)

def plate(d,x,y,w,h,emblem=False,visor=False):
    if w<=2 or h<=2: return
    d.rectangle((x,y,x+w-1,y+h-1),fill=VOID)
    d.rectangle((x+1,y+1,x+w-2,y+h-2),fill=STEEL)
    d.line([(x,y+h-1),(x,y+1),(x+1,y)],fill=METAL,width=1)
    d.line([(x+w-1,y),(x+w-1,y+h-1),(x+1,y+h-1)],fill=SHADOW,width=1)
    d.line([(x+1,y+1),(x+w-2,y+1)],fill=EDGE,width=1)
    if h>5:
        d.line([(x+1,y+2),(x+1,y+h-2)],fill=METAL,width=1)
        d.line([(x+w-2,y+2),(x+w-2,y+h-2)],fill=BLACK,width=1)
        d.line([(x+2,y+2),(x+w-3,y+2)],fill=PURPLE,width=1)
        d.line([(x+2,y+h-3),(x+w-3,y+h-3)],fill=PURPLE,width=1)
    if emblem:
        cx=x+w//2
        cy=y+h//2
        d.polygon([(cx,cy-4),(cx+2,cy),(cx,cy+4),(cx-2,cy)],fill=PURPLE)
        d.line([(cx,cy-3),(cx+1,cy),(cx,cy+3),(cx-1,cy)],fill=LUMEN,width=1)
        d.point((cx,cy-2),fill=GLINT)
        d.line([(x+2,y+4),(cx-2,cy-1)],fill=ROYAL,width=1)
        d.line([(x+w-3,y+4),(cx+2,cy-1)],fill=ROYAL,width=1)
    if visor:
        cy=y+3
        d.line([(x+1,cy),(x+2,cy),(x+3,cy+1)],fill=ROYAL,width=1)
        d.line([(x+w-2,cy),(x+w-3,cy),(x+w-4,cy+1)],fill=ROYAL,width=1)
        d.point((x+2,cy),fill=GLINT)
        d.point((x+w-3,cy),fill=GLINT)
        d.line([(x+w//2,y+5),(x+w//2,y+6)],fill=PURPLE,width=1)

def armor_main():
    im=Image.new("RGBA",(64,64),(0,0,0,0))
    d=ImageDraw.Draw(im)
    pieces=[
        (8,0,8,8),(16,0,8,8),(0,8,8,8),(8,8,8,8),(16,8,8,8),(24,8,8,8), # helmet
        (20,16,8,4),(28,16,8,4),(16,20,4,12),(20,20,8,12),(28,20,4,12),(32,20,8,12), # chest
        (44,16,4,4),(48,16,4,4),(40,20,4,12),(44,20,4,12),(48,20,4,12),(52,20,4,12), # right arm
        (36,48,4,4),(40,48,4,4),(32,52,4,12),(36,52,4,12),(40,52,4,12),(44,52,4,12) # left arm
    ]
    for p in pieces: plate(d,*p)
    # helmet focal point: glowing eyes and crown
    plate(d,8,8,8,8,visor=True)
    d.polygon([(9,8),(11,6),(12,8),(13,5),(14,8)],fill=BLACK)
    d.line([(9,10),(10,10)],fill=LUMEN)
    d.line([(13,10),(14,10)],fill=LUMEN)
    # breastplate: amethyst heart, reinforced diagonal sections
    plate(d,20,20,8,12,emblem=True)
    d.line([(21,22),(23,25),(24,25)],fill=ROYAL)
    d.line([(26,22),(24,25)],fill=ROYAL)
    d.line([(22,29),(25,29)],fill=GLINT)
    for x in (17,30,40,52):
        d.line([(x,22),(x,28)],fill=ROYAL)
    for x in (44,36):
        d.line([(x,25),(x+2,27)],fill=LUMEN)
    save(im,"entity/equipment/humanoid/shadow.png",2)
    save(im,"entity/equipment/humanoid_baby/shadow.png",2)

def armor_leggings():
    im=Image.new("RGBA",(64,32),(0,0,0,0))
    d=ImageDraw.Draw(im)
    pieces=[
        (4,0,8,4),(12,0,8,4),(0,4,4,12),(4,4,8,12),(12,4,4,12),(16,4,8,12), # waist
        (4,16,4,4),(8,16,4,4),(0,20,4,12),(4,20,4,12),(8,20,4,12),(12,20,4,12), # leg left
        (20,16,4,4),(24,16,4,4),(16,20,4,12),(20,20,4,12),(24,20,4,12),(28,20,4,12), # leg right
    ]
    for p in pieces: plate(d,*p)
    d.line([(7,6),(8,7),(9,6)],fill=LUMEN)
    d.line([(5,22),(6,25),(5,28)],fill=ROYAL)
    d.line([(21,22),(22,25),(21,28)],fill=ROYAL)
    for x in (4,20):
        d.line([(x,25),(x+3,25)],fill=LUMEN)
    save(im,"entity/equipment/humanoid_leggings/shadow.png",2)

def item(name):
    im=Image.new("RGBA",(32,32),(0,0,0,0))
    d=ImageDraw.Draw(im)
    def line(points,c=PURPLE,width=1): d.line(points,fill=c,width=width,joint="curve")
    def poly(points,c=STEEL): d.polygon(points,fill=c)
    def rect(bounds,c=BLACK): d.rectangle(bounds,fill=c)
    if name=="shadow_sword":
        poly([(5,29),(1,25),(5,21),(9,25)],SHADOW)
        poly([(6,26),(9,29),(14,21),(12,19)],EDGE)
        poly([(12,21),(9,18),(12,15),(15,18)],ROYAL)
        poly([(13,18),(10,15),(24,1),(30,1),(28,8)],BLACK)
        poly([(14,17),(12,15),(25,3),(28,3),(27,7)],PURPLE)
        poly([(16,15),(24,4),(26,4),(21,12)],LUMEN)
        line([(6,20),(12,26)],GLINT,2)
        line([(17,21),(10,14)],ROYAL,3)
        poly([(21,10),(30,1),(25,1)],GLINT)
    elif name in ("shadow_pickaxe","shadow_axe","shadow_shovel","shadow_hoe"):
        line([(6,28),(22,7)],VOID,5)
        line([(8,27),(23,8)],EDGE,3)
        line([(10,26),(23,8)],ROYAL,1)
        if name=="shadow_pickaxe":
            poly([(5,7),(12,4),(23,3),(30,7),(30,12),(25,9),(19,8),(10,12)],VOID)
            poly([(6,7),(15,6),(25,5),(28,7),(23,8),(14,9)],PURPLE)
            line([(9,7),(23,6)],LUMEN)
        elif name=="shadow_axe":
            poly([(16,3),(28,1),(31,8),(27,19),(20,20),(22,13),(17,10)],VOID)
            poly([(19,4),(27,3),(29,8),(26,16),(22,17),(24,10)],ROYAL)
            line([(27,3),(29,8),(26,15)],LUMEN)
        elif name=="shadow_shovel":
            poly([(23,2),(29,5),(30,12),(25,17),(19,14),(19,8)],VOID)
            poly([(23,4),(27,6),(27,12),(24,15),(21,12),(21,8)],ROYAL)
            line([(24,5),(26,8),(25,11)],LUMEN)
        else:
            poly([(7,6),(13,3),(29,4),(29,10),(24,13),(24,8),(13,8)],VOID)
            poly([(9,6),(15,5),(27,6),(27,8),(16,7)],ROYAL)
            line([(14,5),(25,6)],LUMEN)
    elif name=="shadow_helmet":
        poly([(5,11),(9,4),(14,6),(17,2),(22,7),(27,11),(26,24),(23,27),(9,27),(6,24)],VOID)
        poly([(8,12),(12,8),(20,8),(24,13),(24,23),(20,25),(11,25),(8,22)],STEEL)
        poly([(7,7),(11,3),(12,10)],PURPLE)
        poly([(22,9),(24,3),(27,9)],PURPLE)
        poly([(8,15),(13,14),(16,16),(20,14),(24,15),(22,19),(11,19)],BLACK)
        line([(10,16),(13,16)],GLINT,2)
        line([(19,16),(22,16)],GLINT,2)
        poly([(16,11),(18,13),(16,24),(14,13)],PURPLE)
        line([(16,12),(16,22)],LUMEN)
    elif name=="shadow_chestplate":
        poly([(5,7),(10,2),(14,6),(18,6),(22,2),(27,7),(30,16),(26,22),(24,30),(8,30),(6,22),(2,16)],VOID)
        poly([(6,8),(10,5),(13,9),(19,9),(22,5),(26,8),(27,15),(24,18),(23,26),(9,26),(8,18),(5,15)],STEEL)
        line([(6,10),(10,7),(13,12),(19,12),(22,7),(26,10)],ROYAL,2)
        poly([(16,9),(20,15),(16,25),(12,15)],PURPLE)
        poly([(16,11),(18,15),(16,22),(14,15)],LUMEN)
        line([(11,27),(21,27)],EDGE)
        for x in (7,25): rect((x,18,x+2,22),ROYAL)
    elif name=="shadow_leggings":
        poly([(7,3),(25,3),(26,12),(24,30),(17,30),(16,17),(15,30),(7,30),(6,12)],VOID)
        poly([(9,5),(23,5),(24,11),(21,27),(18,27),(17,15),(14,15),(13,27),(9,27),(8,11)],STEEL)
        line([(10,8),(22,8)],LUMEN,2)
        line([(11,16),(11,25)],ROYAL,2)
        line([(21,16),(21,25)],ROYAL,2)
        rect((15,8,17,13),PURPLE)
    elif name=="shadow_boots":
        for off in (0,15):
            poly([(3+off,5),(13+off,5),(14+off,17),(15+off,24),(12+off,28),(1+off,28),(1+off,22),(4+off,19)],VOID)
            poly([(5+off,7),(11+off,7),(12+off,19),(13+off,24),(11+off,26),(3+off,26),(3+off,22),(5+off,18)],STEEL)
            line([(5+off,11),(11+off,11)],ROYAL,2)
            line([(4+off,23),(12+off,23)],LUMEN)
    elif name.endswith("spawn_egg"):
        if "wither" in name: main=PURPLE; accent=LUMEN
        elif "warden" in name: main=(25,101,116,255); accent=(75,223,230,255)
        else: main=(80,51,112,255); accent=PINK
        d.ellipse((7,3,25,29),fill=VOID,outline=EDGE,width=2)
        d.ellipse((9,5,23,27),fill=main)
        for x,y in [(13,10),(19,15),(12,21),(20,23)]: rect((x,y,x+2,y+2),SHADOW)
        for x,y in [(15,8),(12,17),(18,22)]: rect((x,y,x+1,y+1),accent)
        line([(11,10),(16,15),(14,20)],GLINT)
    elif name=="shadow_wither_core":
        poly([(16,2),(27,8),(26,24),(16,30),(6,24),(5,8)],VOID)
        poly([(16,4),(24,9),(23,23),(16,27),(8,23),(8,9)],PURPLE)
        poly([(16,8),(22,16),(16,24),(10,16)],LUMEN)
        poly([(16,10),(19,16),(16,22),(13,16)],GLINT)
        line([(5,9),(10,6),(12,9),(16,6),(20,9),(23,6),(27,10)],EDGE,2)
    elif name=="shadow_warden_heart":
        poly([(16,10),(10,4),(4,7),(3,15),(16,29),(29,15),(27,7),(22,4)],VOID)
        poly([(16,13),(10,7),(7,9),(7,15),(16,24),(25,15),(25,9),(22,7)],(20,106,131,255))
        poly([(16,14),(12,10),(10,13),(16,22),(22,13),(20,10)],(68,226,246,255))
        line([(16,17),(16,23)],GLINT)
        for x in (7,25): rect((x,11,x+1,13),ROYAL)
    elif name=="shadow_knight_sigil":
        poly([(16,1),(28,9),(28,22),(16,30),(4,22),(4,9)],VOID)
        poly([(16,4),(25,10),(25,20),(16,26),(7,20),(7,10)],STEEL)
        poly([(16,6),(21,12),(16,20),(11,12)],PURPLE)
        line([(16,6),(16,22)],LUMEN,2)
        line([(9,17),(23,17)],ROYAL)
        for x in (8,23): d.point((x,12),fill=GLINT)
    else:
        d.ellipse((6,6,25,25),fill=ROYAL,outline=VOID,width=2)
    save(im,"item/"+name+".png",scale=2)

def icon():
    im=Image.new("RGBA",(64,64),VOID)
    d=ImageDraw.Draw(im)
    d.rectangle((2,2,61,61),outline=ROYAL,width=3)
    d.polygon([(32,6),(57,29),(34,57),(8,33)],fill=METAL)
    d.polygon([(32,10),(50,30),(32,52),(14,31)],fill=PURPLE)
    d.polygon([(32,16),(43,31),(32,46),(20,31)],fill=LUMEN)
    d.polygon([(32,21),(39,31),(32,41),(26,31)],fill=GLINT)
    save(im,"../icon.png",scale=1)

def register_trophies():
    for key in ("shadow_wither_core","shadow_warden_heart","shadow_knight_sigil"):
        p=ROOT/"items"/(key+".json")
        p.parent.mkdir(parents=True,exist_ok=True)
        p.write_text(json.dumps({"model":{"type":"minecraft:model","model":"schattenarsenal:item/"+key}},indent=2)+"\n")
        model=ROOT/"models/item"/(key+".json")
        model.parent.mkdir(parents=True,exist_ok=True)
        model.write_text(json.dumps({"parent":"minecraft:item/generated","textures":{"layer0":"schattenarsenal:item/"+key}},indent=2)+"\n")

def main():
    armor_main()
    armor_leggings()
    for name in (
        "shadow_helmet","shadow_chestplate","shadow_leggings","shadow_boots",
        "shadow_sword","shadow_pickaxe","shadow_axe","shadow_shovel","shadow_hoe",
        "shadow_wither_spawn_egg","shadow_warden_spawn_egg","shadow_knight_spawn_egg",
        "shadow_wither_core","shadow_warden_heart","shadow_knight_sigil"):
        item(name)
    register_trophies()
    print("Schatten-Arsenal: 18 redesigned high-contrast pixel-art textures plus 3 trophy models generated.")

if __name__=="__main__":
    main()
