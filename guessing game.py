import random

x=random.randrange(1,2)
#it was stuck between one and two for testing, i beieve the original was a guess between 1-10

number=int(input('enter your choice: '))

if(number==x):
    print('yay you won')

elif(number >x):
    print("bruh it's more than the number")

elif(number < x):
    print('it was less')
