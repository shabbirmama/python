# -*- coding: utf-8 -*-
"""
Created on Wed Nov 21 11:17:09 2018

@author: hp
"""

'''a=5
while(a>0):
    print("inside while loop")
    print("Hello", a)
    a=a-3
    if(a<0):
        print("break from the loop")
        break
print("Loop Over!")

n=1
while(n<5):
    print("Square of", n, "is", n*n)
    n+=1
print("Thank You!!")

num=int(input("Enter any number: ")) #5
fact=1
a=1
while(a<=num):
    fact*=a     #fact=fact*a
    #print("fact value",fact)   
    a+=1   #2,3,4,5,6
    #print("value of a",a)
print("the factorial of", num, "is", fact)'''

n=int(input("Enter upto which natural number u want to calculate sum: "))
ctr=1
sum_even = sum_odd = 0
while(ctr<=n):  #for I in range(1,n)
	if(ctr%2==0):
		sum_even+=ctr
	if(ctr%2!=0):
		sum_odd+=ctr
	ctr+=1
print("the sum of even integers is: ", sum_even)
print("the sum of odd integers is: ", sum_odd)
