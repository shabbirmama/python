a = input("Enter the first number: ")
b = input("Enter the second number: ")
c = input("Enter the third number: ")

if (a > b):
    if a > c:
        print(a, "is the largest of three")
    elif c > b:
        print(c, "is the largest of three")
elif b > a:
    if b > c:
        print(b, "is the largest of three")
