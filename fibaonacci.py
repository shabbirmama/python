# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 12:52:30 2018

@author: hp
"""

first = 0
second = 1
print(first, end=' ')
print(second, end=' ')
for i in range(1,20):
    third=first+second
    print(third, end=" ")
    first,second=second,third
print("......")