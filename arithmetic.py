num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
op = input("Enter operator [+-*/%]: ")

result = 0
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op =='/':
    result = num1 /num2
elif op == '%':
    result = num1 % num2
else:
    print("Invalid Operator")

print(num1,op,num2,'=', result)