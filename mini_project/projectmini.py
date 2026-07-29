#GUESS THE TARGET NO. (TARGET NO IS 36)

import random

target = random.randint(1,100)

while True:
    userchoice = int(input("guess the target"))
    if(userchoice == target):
        print("yehhhhh..its a correct guess")
        break
    elif(userchoice < target):
        print("you guess is too small....take a bigger guess")
    else:
        print("you guess is too big....take a smaller guess")

print("------GAME OVER-----")            