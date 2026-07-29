#GUESS THE TARGET N0.

import random

target = random.randint(1,100)

while True:
    userchoice = input("guess the target or QUIT : ")
    if(userchoice == "QUIT"):
        break

    userchoice = int(userchoice)
    if(userchoice == target):
        print("yehhhhh..its a correct guess")
        break
    elif(userchoice < target):
        print("you guess is too small....take a bigger guess")
    else:
        print("you guess is too big....take a smaller guess")

print("------GAME OVER-----")            