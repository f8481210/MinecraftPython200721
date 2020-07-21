# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 14:38:32 2020

@author: User
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()
try:
    blockid = int(input("你要放的方塊ID:"))
    mc.setBlock(x+1,y,z,blockid)
except:
    print("只可以輸入數字!!!!!!!!!!!!")
