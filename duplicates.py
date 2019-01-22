a = [10,20,30,20,10,50,60,40,80,50,40, 10]

#dup_items = set
b = [34,56,78,12,34,56,89,90,5,12]
flag = 0
#print(uniq_items)
for i in a:
    if i in b:
        flag = 1
        break
    else:
        flag = 0

if flag == 1:
    print("True!! both the lists have common member")
else:
    print("False!! No common member!!")
"""a = [10, 20, 30, 20, 10, 50, 60, 40, 80, 50, 40, 10]
uniq_items = []
#c = 0
for x in a:
    if x not in uniq_items:
        uniq_items.append(x)
        print("The number of times", x, "is present in the list is: ", a.count(x))

#print(dup_items)
#print(a.count(10))
print("List after removing duplicates: ")
print(uniq_items)"""