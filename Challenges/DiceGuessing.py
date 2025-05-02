import random

playerNumber = int(input("Chose a number between 2 & 12:"))

while playerNumber > 12:
    playerNumber = int(input("The number is bigger than 12, try again:"))


dice1 = random.randint(1, 6)
dice2 = random.randint(1, 6)

plusDices = dice1 + dice2

print(
    f"Dice 1: {dice1}\nDice 2: {dice2}\nThe Sum: {plusDices}\nYour Number: {playerNumber}"
)

if playerNumber == plusDices:
    print("Excellent job, You Win")

elif playerNumber > plusDices:
    print("You lose, try Again")


elif playerNumber < plusDices:
    print("You lose, try Again")
