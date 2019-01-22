
x = eval(input("Enter the first number: "))
y = eval(input("Enter the second number: "))
z = eval(input("Enter the third number: "))

max = x
if y > max:
    max = y
if z > max:
    max = z
print("The largest of three is ", max)