import random

num = random.randint(10, 13)
ctr = 0
count = 0
while ctr < 3:
    guess = int(input("Guess a number in the range 10 to 15: "))
    count+=1
    if guess == num:
        print("You Won!! ")
        print("The tries it took was", count)
        break
    else:
        #print("Try again!! ")
        ctr+=1

if ctr == 3:
    print("You Lose :( \n The number was", num)
