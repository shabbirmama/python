# to find minimum element from a list of elements with its index

lst = eval(input("Enter the elements: "))
length = len(lst)

min_ele = lst[0]
min_index = 0

for i in range(1,length):
    if lst[i] < min_ele:
        min_ele = lst[i]
        min_index = i

