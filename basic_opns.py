# Menu Driven for all the four operations +,-,*,/

print("########################")
print("Press +: Addition")
print("Press -: Subtraction")
print("Press *: Multiplication")
print("Press /: Division")
print("Press %: Modulus")
print("Press //: Floor Division")
print("########################")

num1 = int(input("Enter the first operand: "))
num2 = int(input("Enter the second operand: "))
op = input("Enter your choice of operator:[+ - * / % //]: ")

result = 0
if op == '+':
    result = num1 + num2
elif op == '-':
    result = num1 - num2
elif op == '*':
    result = num1 * num2
elif op == '/':
    result = num1 / num2
elif op == '%':
    result = num1 % num2
elif op == '//':
    result = num1 // num2
else:
    print("Wrong Choice of an Operator!!")

print(num1,op,num2,'=', result)
