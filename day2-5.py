# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 13:42:54 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
while True:
    x,y,z = mc.player.getTilePos()

    right = mc.getBlock(x+1,y-1,z)
    left = mc.getBlock(x-1,y-1,z)
    front = mc.getBlock(x,y-1,z+1)
    back = mc.getBlock(x,y-1,z-1)

    if right == 9 or left == 9 or \
        front == 9 or back == 9 :
        mc.setBlocks(x-1,y-1,z-1,
                     x+1,y-1,z+1,79)
