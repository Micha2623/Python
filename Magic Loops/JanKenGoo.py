# Create a simple rock-paper-scissors game where the user plays against the computer.
#  Gradually enhance it by adding a scoring system that keeps track of wins, losses, and ties,
#  implementing multiple rounds, and creating a graphical user interface (GUI) with libraries like Tkinter.
import random

print("Welcome to JanKenGoo Game 🤩\n")
options = ["Rock", "Paper", "Scissors"]
rounds = int(input("How many rounds would you like to play? (odd number pls):"))
if rounds % 2 == 0:
    rounds += 1

user_score = 0
machine_score = 0
games = 0


def machine_turn():
    global machineEntrance
    machineEntrance = random.randint(1, 3)
    return machineEntrance


def player_turn():
    global userEntrance
    while True:
        try:
            userEntrance = int(input("Enter your choice (1-rock, 2-paper, 3-scissors): "))
            if 1 <= userEntrance <= 3:
                break
            else:
                print("Invalid choice. Please enter 1, 2 or 3.")
        except ValueError:
            print("Invalid input. Please enter a number (1, 2 or 3).")
    return userEntrance



def punctuation():
    global user_score, machine_score, games
    if machineEntrance == userEntrance:
        print("Tie")
        print(f"{options[userEntrance - 1]} vs {options[machineEntrance - 1]}")
        print(f"Player score: {user_score} vs Machine score: {machine_score}")

    elif (userEntrance - machineEntrance) % 3 == 1:
        user_score += 1
        games += 1
        print(f"Player point")
        print(
            f"Player: {options[userEntrance - 1]} vs Machine: {options[machineEntrance - 1]}"
        )
        print(f"Player score: {user_score} vs Machine score: {machine_score}")

    else:
        machine_score += 1
        games += 1
        print("Machine point")
        print(
            f"Machine: {options[machineEntrance - 1]} vs Player: {options[userEntrance - 1]}"
        )
        print(f"Machine score: {machine_score} vs Player score: {user_score} ")


while user_score < rounds // 2 + 1 and machine_score < rounds // 2 + 1:
    player_turn()
    machine_turn()
    punctuation()

if user_score > machine_score:
    print(f"Player Wins {user_score} vs {machine_score}")
else:
    print(f"Machine Wins {machine_score} vs {user_score}")
