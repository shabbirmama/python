# -*- coding: utf-8 -*-
"""
Created on Sun Nov  4 23:34:01 2018

@author: hp
"""
for i in range(1,10):
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))

    if (b==0):
        print("The denominator should not be zero. Enter again")
        continue
    else:
        c=a/b
        print("the quotient is= ",c)