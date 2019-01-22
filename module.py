# -*- coding: utf-8 -*-
"""
Created on Sat Nov 24 22:19:17 2018

@author: hp
"""

n=int(input("Enter a number: "))
s=0
i=1
while(i<=n):
    s+=i
    print(i,end=' ')
    i+=2
print()
print("The sum of odd numbers is: ", s)

num=int(input("Enter any number greater than 1000: "))  #1234
tnum=num   #tnum=1234
reverse=0
while(tnum>0):
    remainder = tnum % 10    #4 ,3,2,1     
    reverse=(reverse*10) + remainder  #4,43,432,4321
    tnum = tnum // 10   #123,12,1, 
print("Reverse of", num , "is", reverse)