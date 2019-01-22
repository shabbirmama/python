x = eval(input('Please enter the list : '))
lst = list(x)
length = len(x)

max1 = lst[0]  # assuming the max number is the 1st one
for i in range(1, length): # i =1,2
    if max1 > lst[i]:   # max1 =5<7
        max1 = lst[i]
    else:
        continue
print('Smallest element in the list is : ', max1)

