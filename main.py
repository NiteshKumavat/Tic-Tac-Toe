import random


position = [" ", " ", " ", " ", " ", " ", " ", " ", " "]



def player1(name) :
    running = True
    while running :
        answer = int(input(f"{name} Enter the position for X : "))
        if position[answer-1] != " " :
            print(f"Position is taken by {position[answer-1]}")
        elif 0 < answer > 9 :
            print("Enter the valid position")
        else :
            position[answer-1] = "X"
            running = False


def player2(name) :
    running = True
    while running :
        answer = int(input(f"{name} Enter the position for O : "))
        if position[answer-1] != " " :
            print(f"Position is taken by {position[answer-1]}")
        elif 0 < answer > 9 :
            print("Enter the valid position")
        else :
            position[answer-1] = "O"
            running = False

def computer() :
    running = True
    while running:
        answer = random.randint(1, 9)
        if position[answer - 1] != " ":
            print(f"Position is taken by {position[answer - 1]}")
        else:
            position[answer - 1] = "O"
            running = False


def counting(symbol) :
    return position.count(symbol)


def check_win() :
    if position[0] == position[1] == position[2] :
        return position[0]
    if position[3] == position[4] == position[5] :
        return position[3]
    if position[6] == position[7] == position[8] :
        return position[6]
    if position[0] == position[3] == position[6] :
        return position[0]
    if position[1] == position[4] == position[7] :
        return position[1]
    if position[2] == position[5] == position[8] :
        return position[2]
    if position[0] == position[4] == position[8] :
        return position[0]
    if position[2] == position[4] == position[6] :
        return position[2]
    elif counting("X") + counting("O") == 9 :
        return "D"
    else :
        return "C"


def showboard() :
    print("     |     |     ")
    print(f"  {position[0]}  |   {position[1]} |   {position[2]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {position[3]}  |   {position[4]} |   {position[5]}  ")
    print("_____|_____|_____")
    print("     |     |     ")
    print(f"  {position[6]}  |   {position[7]} |   {position[8]}  ")
    print("     |     |     ")



def player_vs_player(player_1, player_2) :
    while True :
        if counting("X") == counting("O") :
            player1(player_1)
            print("\n"*100)
            showboard()
        else :
            player2(player_2)
            print("\n" * 100)
            showboard()

        winner = check_win()
        if winner == "X" :
            print(f"{player_1} is the winner")
            break
        elif winner == "O" :
            print(f"{player_2} is the Winner")
            break
        elif winner == "D" :
            print("No one is the winner")
            break
        else :
            continue


def player_vs_computer(name) :
    while True :
        if counting("X") == counting("O") :
            player1(name)
            print("\n" * 100)
            showboard()
        else :
            computer()
            print("\n" * 100)
            showboard()


        winner = check_win()
        if winner == "X" :
            print(f"{name} is the winner")
            break
        elif winner == "O" :
            print("Computer is the Winner")
            break
        elif winner == "D" :
            print("No one is the winner")
            break
        else :
            continue


if __name__ == "__main__" :
    play = input("Do you want to play the game : (No) or (Yes) : ").title()
    while play == "Yes" :
        print("1. Player vs Player")
        print("2. Player vs Computer")
        game = int(input("Enter the mode of game (1) or (2) : "))
        name_1 = input("Enter the name of the player 1 : ")
        if game == 1 :
            name_2 = input("Enter the name of the player 2 : ")
            print("\n"*100)
            showboard()
            player_vs_player(name_1, name_2)
        elif game == 2 :
            print("\n" * 100)
            showboard()
            player_vs_computer(name_1)
        else :
            print("Enter the valid number ")

        play = input("Do you want to play the game : (No) or (Yes) : ").title()

