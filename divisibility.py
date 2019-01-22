
num1 = int(input("Enter the first integer"))
num2 = int(input("Enter the second integer"))

rem = num1 % num2

if rem == 0:
    print(num1, "is divisible by", num2)
else:
    print(num1, " is not divisible by ", num2)
