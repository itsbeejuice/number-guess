import random

name=input("What is your name contestant? ")
print("Welcome",name,"The goal of this game is to simply guess and I'll tell you if you've won or not!")
lvl=input("We have 3 levels\nbeginner (numbers 1-10)\nmedium (numbers 1-50)\nand\nhard (numbers 1-100)\nPlease choose here:")

if lvl=="beginner":
    x=random.randrange(1,10)
    number=int(input("Enter your choice: "))
    if(number==x):
        print("WINNERRRRRRRRR")
    elif(number>x):
        print("Your number is over the guessed number, sorry. Better luck next time!")
    elif(number<x):
        print("Your number was less than the chosen number sorry, better luck next time!")
    #take loop and look it for lines 11-16 in future updates
elif lvl=="medium":
    x=random.randrange(1,50)
    number2=int(input("Enter your number: "))
    if (number2==x):
        print("WINNERRRRRRRRRRRR")
    elif(number2>x):
        print("Your number was larger than the guessed number, sorry. Better luck next time!")
    elif(number2<x):
        print("Your number was less than the chosen number my apologies!")
        #loop this from lines 22-25
elif lvl=="hard":
    x=random.randrange(1,100)
    number3=int(input("Enter your guess: "))
    if (number3==x):
        print("WINNERRRRRR")
    elif (number3>x):
        print("Your number was larger than our number, better luck next time!")
    elif (number3<x):
        print("Your number was smaller than our guessed number, better luck next time!")
        #loop lines 32-35
