import random

number=random.randint(1,9)
chances=0
print("Guess a number between 1-9")

while chances <5:
    guess=input("guess a number")
    if (number==guess):
        print("You won")

    else :
        print("Try again")

    chances+=1        

    