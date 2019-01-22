lst1 = eval(input("Enter different strings: "))
lst = list(lst1)
ctr = 0
for word in lst:
    if len(word) > 1 and word[0] == word[-1]:
        print("The elements which are satisfying the criteria are: ")
        print(word)
        ctr+=1

print("No. of elements with same first and last character are:", ctr)
