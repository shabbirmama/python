# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 12:49:26 2018

@author: hp
"""

import random

number=random.randint(10,50)
ctr=0
while(ctr<5): #ctr=4
	guess=int(input("Guess a number in the range 10..50:"))
	if(guess==number):
		print('You Won!!')
		break	
	else:
        #print("You r in else")
		ctr+=1
#if(not ctr<5):
print('You lose:(\n The number was', number)
