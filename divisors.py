# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 13:03:11 2018

@author: hp
"""

num=int(input("Enter any integer: "))
mid=int((num/2)+1)
print("The divisors of", num, "are: ", end=' ')
for a in range(2,mid):
    if(num%a==0):
        print(a, end=' ')
'''else:
    print("--End--")'''
