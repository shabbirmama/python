# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 23:49:57 2018

@author: hp
"""

lst=[4,3,2,0]
for i in range(1,4):
    a=int(input("enter any integer to search in the list: "))
    if a in lst:
        print("Number",a, "is found in the list")
        break
    else:
        print("number not present in ", lst,"Good bye")
        break
else:
    print("The loop is executed")
    