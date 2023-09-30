	#
#     _______________ __  __
#    / ____/  _/ ___// / / /
#   / /_   / / \__ \/ /_/ / 
#  / __/ _/ / ___/ / __  /  
# /_/   /___//____/_/ /_/   
#
# Fish Interface for Super Hacks
#

import playsound as p
import time
from mcpi_addons.minecraft import Minecraft
import random

hacks = []
hacknames = []
p.playsound('./beast.mp3', False)
mc = Minecraft.create()

mc.postToChat("F.I.S.H has LOADED\n")

def get_input(msg: str):
    return input("\033[1;33m[F.I.S.H]\033[1;37m " + msg)
    
def add_hack(function, name: str):
    hacks.append(function)
    hacknames.append(name)
    
def tnt_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 46)
        time.sleep(0.01)
add_hack(tnt_feet, "TNT Feet")
def water_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 8)
        time.sleep(0.01)
add_hack(water_feet, "Water Feet")
def lava_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 10)
        time.sleep(0.01)
add_hack(lava_feet, "Lava Feet")
def noah_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x - 2, y, z - 2, x + 2, y, z + 2, 8)
        time.sleep(0.01)
add_hack(noah_feet, "Noah ark")
def life_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x - 2, y -1, z - 2, x + 2, y-1, z + 2, 12)
        time.sleep(0.01)
add_hack(life_feet, "Life a beach")
def gravil_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x - 2, y -1, z - 2, x + 2, y-1, z + 2, 13)
        time.sleep(0.01)
add_hack(gravil_feet, "Life is gravel")
def jardin_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 38)
        time.sleep(0.01)
add_hack(jardin_feet, "flowers are plentiful")
def jardin2_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 37)
        time.sleep(0.01)
add_hack(jardin2_feet, "flowers are plentiful again")
def color_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 35,random.randrange(0,15))
        time.sleep(0.01)
add_hack(color_feet, "the feet are rainbows")
def nucker():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x - 5, y+5, z - 5, x + 5, y-5, z + 5, 0)
        time.sleep(0.01)
add_hack(nucker, "Nuker hack")
def light_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 50)
        time.sleep(0.01)
add_hack(light_feet, "path shower")
def cold_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y-1, z, 79)
        time.sleep(0.01)
add_hack(cold_feet, "frost walker")
def gitch_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y-1, z, 95)
        time.sleep(0.01)
add_hack(gitch_feet, "shoe are gitch")
def explod_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x - 2, y -1, z - 2, x + 2, y-1, z + 2, 46, 1)
        time.sleep(0.01)
add_hack(explod_feet, "evil bomber")
def spammer():
    spam = get_input("what are you spam? ")
    while True:
        mc.postToChat("F.I.S.H spammer: " + spam)
        time.sleep(0.01)
add_hack(spammer, "spammer")
def rspammer():
    while True:
        mc.postToChat("F.I.S.H spammer: " + str(random.randbytes(100)))
        time.sleep(0.01)
add_hack(rspammer, "random spammer")
def r2spammer():
    while True:
        mc.postWithoutPrefix("F.I.S.H spammer: " + str(random.randrange(0,2912849134124132412412414124)))
        time.sleep(0.01)
add_hack(r2spammer, "super random spammer")
def cameraspy():
    while True:
        mc.camera.setFollow(random.randrange(0,128))
        time.sleep(0.01)
add_hack(cameraspy, "cameraspy")
def falsechat():
    name = get_input("what are you impersonate? ")
    while True:
        msg = get_input("what to say ")
        mc.postWithoutPrefix("<" + name + "> " + msg)
add_hack(falsechat, "player impersonate")
def spamtnt():
    while True:
        x, y, z = mc.player.getPos()
        mc.entity.spawn(65, x, y, z, 0)
        time.sleep(0.01)
add_hack(spamtnt, "SPAM TNT")
def art():
    while True:
        x, y, z = mc.player.getPos()
        mc.entity.spawn(12, x, y, z, 0)
        time.sleep(0.1)
add_hack(art, "PIGGS")
def godmode():
    while True:
        mc.player.setHealth(100)
        time.sleep(0.1)
add_hack(godmode, "GOD MODE UNKILLABLE")
def die():
    mc.player.setHealth(0)
add_hack(die, "DIE")
def sticky_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(x - 2, y -1, z - 2, x + 2, y-1, z + 2, 30)
        time.sleep(0.01)
add_hack(sticky_feet, "spider spray")
def autoclicker():
    mc.player.press("w")
add_hack(autoclicker, "autowalker")
def autoclicker():
    mc.player.release("w")
add_hack(autoclicker, "stop autowalker")
def compass_feet():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x - 2, y -1, z - 2, x + 2, y-1, z + 2, 35, 15)
    mc.setBlocks(x, y -1, z, x + 2, y-1, z, 35, 14)
    mc.setBlock(x, y, z, 50)
add_hack(compass_feet, "compass point to north")
def penis_builder():
    x, y, z = mc.player.getPos()
    mc.setBlocks(x + 1, y + 1, z, x + 1, y + 2, z, 7)
    mc.setBlocks(x + 1, y, z - 1, x + 1, y, z + 1, 7)
    mc.setBlocks(x + 1, y, z, x + 1, y, z, 0)
add_hack(penis_builder, "build penid")
def scaffold():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y-1, z, 7)
        time.sleep(0.01)
add_hack(scaffold, "Scaffold")
def fire_feet():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y, z, 11, 7)
        mc.player.setHealth(100)
        time.sleep(0.1)
add_hack(fire_feet, "lava man")
def gitch_grower():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlock(x, y-1, z, 60, 15)
        mc.setBlock(x, y, z, 59, 10)
        time.sleep(0.01)
add_hack(gitch_grower, "gitch grower")
def WORLDKILLER():
    while True:
        x, y, z = mc.player.getPos()
        mc.setBlocks(-128, y - 1,-128, 128, y + 1, 128, 0)
        time.sleep(0.01)
add_hack(WORLDKILLER, "world slicer")
def WORLDKILLER2():
    x, y, z = mc.player.getPos()
    mc.setBlocks(-128, y - 1,-128, 128, y - 3, 128, 11)
    mc.setBlock(x, y -1, z, 7)
add_hack(WORLDKILLER2, "lava lands")
def WORLDKILLER3():
    x, y, z = mc.player.getPos()
    mc.setBlocks(-128, y - 1,-128, 128, y - 3, 128, 46, 1)
    mc.setBlock(x, y -1, z, 7)
add_hack(WORLDKILLER3, "tnt lands")
    
hacklist = "HACKLIST"
for index, element in enumerate(hacks):
    hacklist = hacklist + "\033[1;37m, " + str(index) + ": \033[1;33m" + hacknames[index]
print(hacklist + "\n")
while True:
    hacks[int(get_input("Choose hack "))]()

    
