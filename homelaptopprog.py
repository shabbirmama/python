# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.


x = 40
y = 30
z = 

if(x>y):
    if (x>z):
        print('x is big')
if(y>x):
    if (y>z):
        print('y is big')
if(z>x):
    if (z>y):
        print('z is big')
        
x = 20
y = 30
z = 40

if(x>y):
    if(x>z):
        print(x," is the biggest number")
    else:
        print(z, "is the biggest number")
elif(y>x):
    if(y>z):
        print(y,"is the biggest number")
    else:
        print(z, "is the biggest number")
        
        -----------------------------
ch = input('Enter a single character: ')
if(ch>='A' and ch<='Z'):
    print('You have entered a uppercase character')
elif(ch>='a' and ch<='z'):
    print('You have entered a lowercase chracter')
elif(ch>='0' and ch<='9'):
    print('You have entered a digits')
else:
    print('You have entered a special character')
    
    x = int(input('Enter the first number: '))
y = int(input('Enter the second number: '))
z = int(input('Enter the third number: '))

if (x<y and x<z):
  if (y<z):
      min, med, max = x, y, z
  else: 
      min, med, max = x, z, y
if (y<x and y<z):
    if(x<z):
        min, med, max = y, x, z
    else:
        min, med, max = y, z, x
if (z<x and z<y):
    if(x<y):
        min, med, max =  z, x, y
    else:
        min, med, max = z, y, x

print(min, med, max)
    


thislist=['apple', 'orange', 'grapes', 'lime']
thislist.remove("lime")
print(thislist)



for hh in ("This is shabbir"):
    print(hh)


line = input("enter line: ")
word = input("enter word: ")
if word in line:
    print(word, "present")
else:
     print(word, "absent")
     
     
     -------------------
     or i in range( len(wordList) - 1, -1, -1) :
        print(wordList[i])
        
    print("*************")    
    
    '''
     Iterate over the list using for loop and reversed()
    '''
  
     
     
word = 'shabbir'     
for i in reversed(word):
    print(i)
    
    --------------------
    
    

num=int(input('Enter the number :'))
for i in range(num, 1, -1):
    print(num)

   
num = 30
ctr = int(num/2)+1
for i in range(2, ctr):
    kol=num%i
    if(kol == 0):
        print(num, 'Not a prime number')
        break
else:
    print(num,'Not a Prime Number')


  
    ch = input('Enter a single character: ')
if(ch>='A' and ch<='Z'):
    print('You have entered a uppercase character')
elif(ch>='a' and ch<='z'):
    print('You have entered a lowercase chracter')
elif(ch>='0' and ch<='9'):
    print('You have entered a digits')
else:
    print('You have entered a special character')

----------

if (veg==potato):
    print('You have consumed:', potato, 'calories')
elif veg==tomato:
    print('You have consumed:', tomato, 'calories')
elif veg==onion:
    print('You have consumed:', onion, 'calories')
    



potato=100
tomato=50
onion=25

veg = input('Please choose one of these vegies: potato or tomato or onion: ')

if (veg=='potato'):
    print('You have consumed:', potato, 'calories')
elif veg=='tomato':
    print('You have consumed:', tomato, 'calories')
elif veg=='onion':
    print('You have consumed:', onion, 'calories')
     
       
x=int(input('Please Enter a number : '))
y=int(input('Please Enter a power number : '))
z=y+1
sum=0
for i in range(1,z):
    a=x**i
    sum=sum+a
print(1+sum)

----------
x=int(input('Please Enter a number : '))
y=2
sum=0
for i in range(1,x,2):
    z=i**2
    sum=sum+z
print(sum)


  """













      
       

       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
       
    
  
    


































































































        