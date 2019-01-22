# Selection Sort

lst1 = eval(input("Enter the numbers separated by comma: "))
lst = list(lst1)

l1 = len(lst)
"""for i in range(0, l1):     # 0,1
    for j in range(i+1, l1):    # 1,2,3,4
        if lst[i] > lst[j]:
            lst[i], lst[j] = lst[j], lst[i]

print("The list in ascending order is: ")
print(lst)

# Insertion Sort
for i in range(1, l1):
    key = lst[i]
    j = i-1
    while j >= 0 and key < lst[j]:
        lst[j+1] = lst[j]
        j-=1
    lst[j+1]=key

print("The list in ascending order is: ")
for i in range(len(lst)):
    print("%d" %lst[i])"""

# Bubble Sort
for i in range(l1):
    for j in range(0, l1-i-1):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

print("the elements in ascending order is: ")
print(lst)