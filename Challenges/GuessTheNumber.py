import random

player_one = input("Name of the player one: ")
player_two = input("Name of the player two: ")

max = int(input("Set the TOP: ")) #Max number
randomNumber = int(random.randint(1, max)) #chose a number between 1 and the max
p1_tries = 0 
p2_tries = 0


def p1_turn():
    userNumber = int(input(f"{player_one}, Enter a number: "))
    global p1_tries
    p1_tries += 1
    if userNumber > randomNumber:
        print(f"You've failed! The number is lower than {userNumber}, try again")
        return
    elif userNumber < randomNumber:
        print(f"You've failed! The number is bigher than {userNumber}, try again")
        return
    else:
        print(f"{player_one} Wins\nIt took {p1_tries} tries")
        quit()


def p2_turn():
    userNumber = int(input(f"{player_two}, Enter a number: "))
    global p2_tries
    p2_tries += 1
    if userNumber > randomNumber:
        print(f"You've failed! The number is lower than {userNumber}, try again")
        return
    elif userNumber < randomNumber:
        print(f"You've failed! The number is bigher than {userNumber}, try again")
        return
    else:
        print(f"{player_two} Wins\nIt took {p2_tries} tries")
        quit()


while True:
    p1_turn()
    p2_turn()


