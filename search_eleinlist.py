ele = eval(input("Enter the numbers, separated by comma: "))
a = list(ele)
x = int(input("Enter the number to be searched: "))
i = 0; pos = 0
length = len(a)
while i < length:  # 0,1
    if a[i] == x:
        pos = i
        print("Element is present in the list at index", pos)
        break
    i += 1
else:
    print("Number is not present in the list!!")

