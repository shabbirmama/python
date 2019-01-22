x = eval(input("Enter the numbers, separated by comma: "))
lst = list(x)
print("The list elements are", lst)

sum_ele = 1
length = len(lst)

for i in range(0,length): # 0->3, 1
    sum_ele*=lst[i]  # sum_ele = sum_ele * lst[i]

print("The sum of the elements of a list is", sum_ele)

