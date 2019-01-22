"""L = ['q', 'w', 'e', 'r', 't', 'y']

length = len(L)

for a in range(length):
    print("At indexes", a, "and", (a-length), "element:" , L[a])"""

lst = [1, 2, 3, 4, 5, 6, 7, 8,9,10,11,12,13,14,15,16,17,18,19,20]

slc1 = lst[5:15:2]
slc2 = lst[::4]

sum1 = avg = 0

for a in slc1:
    sum1+=a
    print(a, end=',')
print()

print("sum of slice 1: ", sum1)

sum1 = 0
for a in slc2:
    sum1+=a
    print(a, end=',')
print()

avg = sum1/len(slc2)
print("Average of slice 2 is: ", avg)
