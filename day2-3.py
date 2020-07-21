# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 10:32:01 2020

@author: User
"""


from mcpi.minecraft import Minecraft
mc = Minecraft.create()
x,y,z = mc.player.getTilePos()

height = 10 #高
lenght = 10 #長
width = 10  #寬

mc.setBlocks(x,y,z,x+width,
             y+height,z+lenght,46)
mc.setBlocks(x+1,y+1,z+1,x+width-1,
             y+height-1,z+lenght-1,0)