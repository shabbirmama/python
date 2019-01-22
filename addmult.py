'''x=int(input('Please Enter a number: '))
y=int(input('Please Enter a number: '))
z=0
ctr=0
while(z<y):#0,1
    ctr+=x #ctr=0+25=25,
    z+=1
print("The product of ", x,"and", y, "is", ctr)

ctr=0
x=0
guess = "done"
while(ctr<5):
    guess = input('Please Enter the number or say done : ')
    #y=int(guess)
    if(int(guess)>0):
        x+=int(guess)
        print(x)
    elif(guess == "done"):
        print(guess, 'is typed')
        break
    else:
        print('wrong word')
    ctr+=1'''

answer = 23
question = 'What number am I thinking of?  '
print( 'Let\'s play the guessing game!' )

while True:
    guess = int( input( question ) )

    if guess < answer:
        print( 'Little higher' )
    elif guess > answer:
        print( 'Little lower' )
    else:  # guess == answer
         print( 'MINDREADER!!!' )
