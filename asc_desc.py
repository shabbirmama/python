# Program that reads three numbers(integers) and prints them in ascending order

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))
z = int(input("Enter the third number: "))

minn = mid = maxx = None

if x < y and x < z:
    if y < z:
        minn, mid, maxx = x, y, z
    else:
        minn, mid, maxx = x, z, y
elif y < x and y < z:
    if x < z:
        minn, mid, maxx = y, x, z
    else:
        minn, mid, maxx = y, z, x
else:
    if x < y:
        minn, mid, max = z, x, y
    else:
        minn, mid, max = z, y, x

print("Numbers in ascending order are ", minn, mid, maxx)