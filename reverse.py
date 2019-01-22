# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 12:11:53 2018

@author: hp
"""
import random


x = random.randrange(2000, 2003)
ctr=0
while(ctr < 3):
    y=int(input('Please guess a number between 2000 and 2200 : '))
    if (x==y):
        print('You are the winner')
        break
    else:
        print('Try Again :' )
        ctr+=1
#print('"You lost" The number was', x)
print('"GAME OVER" ! The number was', x)
