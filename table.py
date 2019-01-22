# program to print table of a number

num = int(input("Enter any number: "))

for a in range(1,11):
    print(num,'x',a, '=', num*a)

# program to print sum of natural numbers between 1 and 7

sum1 = 0
n = None
for n in range(1, 8):
    sum1+=n
print("Sum of", n, "natural numbers is", sum1)

# program to print progressive sum
sum1 = 0
for n in range(1, 8):
    sum1+=n
    print("Sum of", n, "natural numbers is", sum1)

# program to show the working of break statement

a = b = c = 0
for i in range(1, 8):
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    if b == 0:
        print("Division by Zero Error!! ABORTING")
        break
    else:
        c = a / b
        print("Quotient = ", c)
print("Program Over!")

import random
import math

number = random.randint(1, 5)
for i in range(5): # i=1,2,3,4,5
    guess = int(input("Guess any number in the range 1...5: "))
    if guess == number:
        print("You Win!! ")
        break
if i == 5:
    print("You lose :( \n The number was", number)

# program to show the working of continue statement

a = b = c = 0

for i in range(0,3): # i = 0,1,2
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    if b == 0:
        print("The denominator cannot be zero. Enter again!!")
        continue
    else:
        c = a / b
        print("Quotient is ", c)
print("Loop Ended!!")

# program to illustrate difference between break and continue statement

print("The loop with break produces output as: ")
for i in range(1,11): # i = 1,2,3
    if i % 3 == 0:
        break
    else:
        print(i)

print("Loop with continue produces output as: ")
for i in range(1,6): # 1 = 1,2,3,4,5
    if i % 3 == 0:
        print("Before continue!!")
        continue
    else:
        print(i)
print("Loop ended!!")

# program to illustrate for-else

for i in range(1,4):
    print("Element is", i, end =' ')
    continue
    #print(i)
else:
    print()
    print("Ending loop after printing all elements of a sequence!!")

# program to print grades based on percentage

for i in range(0,5):
    grade = float(input("What's the grade percentage?: "))
    if grade >= 90:
        print("Your grade is A+!!")
    elif 80 <= grade < 90:
        print("Your grade is A!!")
    elif 60 <= grade < 80:
        print("Your grade is A- !!")
    else:
        print("Below any standard!!")

a = 5
while a > 0:
    print("Hello", a)
    a = a - 3  # a-=3
print("Loop Over!!")

n = 1
while n < 5:
    print("Square of", n, "is", n**2)
    n+=1
print("Thank You!!")



