# -*- coding: utf-8 -*-
"""
Created on Thu Nov  8 11:41:58 2018

@author: hp
"""

num=int(input("Enter a number: "))
"""ctr=num-1
for i in range(ctr,0,-1):
    temp=num
    num*=i
    print(temp,'X',i,'=',num)"""
    
fact = 1
a = 1
while a <= num:
    fact*=a
    a+=1
print("The factorial of", num, "is", fact)