# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 11:15:53 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
import time,random

#題目：我邊走，不同的花一直出現！
while True :
    x,y,z = mc.player.getTilePos()
    color = random.randrange(0,9)
    mc.setBlock(x,y,z-1,38,color)
    time.sleep(0.2)
    