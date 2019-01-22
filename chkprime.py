# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 12:09:51 2018

@author: hp
"""
import math

num = int(input("Enter any number to be checked: "))
lim = int(math.sqrt(num)+1)
for i in range(2, lim):
    rem = num % i
    if rem == 0:
        print({}.format(num), "is not a prime number")
        break
else:
    print(num, "is a prime number") 
