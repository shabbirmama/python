#program to input numbers repeatedly and print the sum. The program ends when the user says no or program aborts when the number entered is less than 0

sum1 = count = 0
ans = 'y'
while ans == 'y':
    num = int(input("Enter any number: "))
    if num < 0:
        print("Number entered is below zero. Aborting!!")
        break
    sum1+=num
    count+=1
    ans = input("Want to enter more number(y/n): ")
else:
    print("You entered", count, "numbers so far.!!")
print("The sum of numbers entered is", sum1)

