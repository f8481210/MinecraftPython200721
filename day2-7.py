# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 15:07:35 2020

@author: User
"""

from mcpi.minecraft import Minecraft
mc = Minecraft.create()
username = input("請輸入名字:")
#題目:我想一直說話
while True:
    
    message = input("輸入訊息:")

    mc.postToChat("["+username+"]"+message)
