import random

x=random.randrange(1,2)

number=int(input('enter your choice: '))

if(number==x):
    print('yay you won')

elif(number >x):
    print("bruh it's more than the number")

elif(number < x):
    print('it was less')
