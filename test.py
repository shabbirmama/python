"""n = int(input("Enter any integer less than 10: "))

print("square of", n ,"is", n ** 2)
print("cube of", n ,"is", n ** 3)
print(n,"to the power 4 is equal to ", n ** 4)

name = input("Enter ur name: ")
age = int(input("Enter ur age: "))
cls = int(input("Enter ur class: "))

print("Name is", name, "Age is", age, "Class is", cls)
print()
print()
print("Name is", name)
print()
print()
print("Age is", age)
print()
print()
print("Class is", cls)

n = int(input("Enter the number: "))
print("Printing first 5 multiples of", n)
print(n * 1)
print(n * 2)
print(n * 3)
print(n * 4)
print(n * 5)

# Celsius to fahrenheit

cels = float(input("Enter the temperature in Celsius: "))
print("The temperature in Celsius is", cels)
fahr = cels * 9 / 5 + 32
print("Temperature in Fahrenheit is", fahr)

# input a number and print two consecutive numbers following it

n = int(input("Enter any single digit number: "))

print("You entered", n)
print("Three consecutive numbers in a row are", n, end = "")
print(n+1, end = "")
print(n+2)

n = 100

if n < 100:
    print("value of n is less than 100!!")
elif n > 100:
    print("Value is greater than 100!!")
    if n > 100 & n < 200:
        print("value of n is greater than 100 but less than 200!!")
    else:
        print("n is greater than 200!!")
else:
    print("value is equal to 100")
print("finish!!")

#python project to find largest number among 3 given numbers
num1= int(input("enter the first number: "))
num2= int(input("enter the second number: "))
num3= int(input("enter the third number: "))
if(num1>num2) and (num1>num3):
    print(num1, " is the greatest")
elif(num2>num1) and (num2>num3):
    print(num2, " is the greatest")
else:
    print(num3, " is the greatest")

x = 1
if x > 3:
    if x > 4:
        print("A", end=' ')
    else:
        print("B", end=' ')
elif x < 2:
    if x!= 0:
        print("C", end=' ')
print("D")

weather = input("Enter the weather condition, whether its raining, its sunny or snow: ")

if weather == 'sunny':
    print("Wear sunblock!!")
elif weather == 'snow':
    print("Go Skiing!!")
else:
    print("Its", weather, "!! So go inside home and study!!")

if float(0.15) == 0:
    print("Zero!!")
elif str(0) == 'zero':
    print(0)
elif str(0) == '0':
    print(str(0))
else:
    print("None of the above!!")

if n == 0:
    print("zero")
elif n == 1:
    print("one")
elif n == 2:
    print("two")
else:
    print("three")

line = input("Enter a line: ")
string = input("Enter a string: ")
if string in line:
    print(string, "is a part of", line)
else:
    print(string, "not a part of ", line)

for a in range(1, 8, 3):
    print(a)
    print(a*a)
print("Out of loop!!")

for ch in 'calm is':
    print(ch)

print("HELLO WORLD!!")"""

# Python program to demonstrate
# Creation of List

# Creating a List
List = []
print( "Intial blank List: " )
print( List )

# Creating a List with
# the use of a String
List = ['GeeksForGeeks']
print("\nList with the use of String: ")
print(List)

# Creating a List with
# the use of multiple values
List = ["Geeks", "For", "Geeks"]
print( "\nList containing multiple values: ")
print(List[0])
print(List[2])

# Creating a Multi-Dimensional List
# (By Nesting a list inside a List)
List = [1, 2, ['Geeks', 'For', 'Geeks'], 3, 4, ['Geeks']]
print(List[2][0])
print("\nMulti-Dimensional List: ")
print(List)

# Creating a List with
# the use of Numbers
# (Having duplicate values)
List = [1, 2, 4, 4, 3, 3, 3, 6, 5]
print( "\nList with the use of Numbers: " )
print( List )

# Creating a List with
# mixed type of values
# (Having numbers and strings)
List = [1, 2, 'Geeks', 4, 'For', 6, 'Geeks']
print( "\nList with the use of Mixed Values: " )
print( List )



