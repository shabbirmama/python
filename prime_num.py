# program to input a number  and check whether its prime or not

"""num = int(input("Enter any number: "))
lim = (num // 2) + 1
#print(lim)
for i in range(2, lim):
    rem = num % i
    if rem == 0:
        print(num, "is not a prime number!!")
        break
else:
    print(num,"is a prime number!!")"""

# Python program to demonstrate
# Addition of elements in a List

# Creating a List
List = []
print( "Intial blank List: " )
print( List )

# Addition of Elements
# in the List
List.append(1)
List.append(2)
List.append(4)
print("\nList after Addition of Three elements: ")
print(List)

# Adding elements to the List
# using Iterator
for i in range(1, 4):
    List.append(i)
print( "\nList after Addition of elements from 1-3: ")
print( List)

# Adding Tuples to the List
List.append((5, 6))
print("\nList after Addition of a Tuple: " )
print(List)

# Addition of List to a List
List2 = ['For', 'Geeks']
List.append(List2)
print( "\nList after Addition of a List: " )
print(List)
print(List2)

# Addition of Element at
# specific Position
# (using Insert Method)
List.insert(3, 12)
List2.insert(0, 'Geeks')
print( "\nList after performing Insert Operation: " )
print( List )

# Addition of multiple elements
# to the List at the end
# (using Extend Method)
List.extend([8, 'Geeks', 'Always'])
print( "\nList after performing Extend Operation: " )
print( List )