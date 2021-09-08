# Program to play stone payer and scissor.
import random

"""
    1 for Stone
    2 for Paper
    3 for Scissor
"""
print("Enter 1 for Stone\nEnter 2 for Paper\nEnter 3 for Scissor \n\n")

randomList = ['Stone', 'Paper', 'Scissor']
playerWin = 0
computerWin = 0

for i in range(5):
    randomChoice = random.randint(1, 3)
    userInput = int(input("Enter your choice: "))
    # player input == Stone
    if userInput == 1:
        if randomChoice == 1:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Both choice same, Tie")
        elif randomChoice == 2:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Computer Win")
            computerWin += 1
        elif randomChoice == 3:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Player Win")
            playerWin += 1
    # player input == Paper
    elif userInput == 2:
        if randomChoice == 2:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Both choice same, Tie")
        elif randomChoice == 3:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Computer Win")
            computerWin += 1
        elif randomChoice == 1:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Player Win")
            playerWin += 1
    # player input == Scissor
    elif userInput == 3:
        if randomChoice == 3:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Both choice same, Tie")
        elif randomChoice == 1:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Computer Win")
            computerWin += 1
        elif randomChoice == 2:
            print("Computer choose : ", randomList[randomChoice - 1])
            print("Player Win")
            playerWin += 1
    else:
        print("Invalid Input")
    print('\n\n')

if computerWin > playerWin:
    print("Sorry! You lose the game with ", (computerWin, playerWin))
elif computerWin < playerWin:
    print("Congrats! you win the game with ", (playerWin, computerWin))
else:
    print("Game tie! with ", playerWin, 'and', computerWin)
