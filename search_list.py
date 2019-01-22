# program to search for an element in a given list of numbers

lst1 = eval(input("Enter the list of numbers separated by comma: "))
lst = list(lst1)
length = len(lst)
element = int(input("Enter the element to be searched for: "))

for i in range(0, length):
        if element == lst[i]:   # i=0,1,2,3,4
            print(element, "found at index", i)
            break
else:
    print(element, "not found in given list")

"""i = 0
while i < length:
    if element in lst[i]:
        print(element, "found at index", i)
        break
    else:
        i += 1
else:
    print( element, "not found in given list")

if element in lst:
    print("element found")
else:
    print( element, "not found in given list" )"""

