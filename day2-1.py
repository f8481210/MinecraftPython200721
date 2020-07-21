# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 09:36:08 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()

x,y,z = mc.player.getTilePos()

mc.setBlock(x,y,z,35,14)
#mc.setBlocks(x+25,y-1,z+25,x-25,y-1,z-25,46)