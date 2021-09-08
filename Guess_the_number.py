#   Number Guess Game
import random

randomNumber = random.randint(1, 101)
rounds = 0

while True:
    userInput = int(input("Enter a number : "))
    if randomNumber == userInput:
        rounds += 1
        print("You have cleared in {} rounds ".format(str(rounds)))
        break
    elif randomNumber > userInput:
        print("Move right")
        rounds += 1
    else:
        print("Move left")
        rounds += 1
