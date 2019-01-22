"""keys = {'a', 'e', 'i', 'o', 'u'}
v = 'vowels'
vowels = dict.fromkeys(keys, v)
print(vowels)


sales = {'apple': 2, 'orange': 3, 'grapes': 4}

#item = sales.values()
#print('Values are', item)

d = 'not found'
print(sales.pop('banana'))

d = {1: "one", 2: "three"}
d1 = {2: "two"}
d.update(d1)
print(d)
d1 = {3: "three"}
d.update(d1)
print(d)
d1 = {12: "two"}
d.update(d1)
print(d)

# Write a Python program to count the number of strings where the string length is 2 or more and the first and last character are same from a given list of strings.
lst1 = eval(input("Enter different strings, separated by comma: "))
lst = list(lst1)
print(lst)

count = 0

for x in lst:
    if len(x) > 1 and x[0] == x[-1]:
        count+=1

print("The number of strings whose length > 2 and have same first and last characters are", count)

lst = [(1, 2), (3, 4), (4, 1), (1, 0), (3, 3)]
last = len(lst)
print(last)
x = sorted(lst, key = last)
print(x)

import itertools

#lst = ['Little']
#print(list(permutations([1,5,8,6])))
x = itertools.compress("Little", [1, 1, 1, 1, 0, 0])
print(list(x))"""

num =[10, 30, 4, -6]
print(num)
x = int(input("Enter the element whose index you want to find: "))
for y in num:    # 10,30,4
    if y == x:
        print("The index of the element entered is", num.index(y))
        break
else:
    print("number not found!!")





