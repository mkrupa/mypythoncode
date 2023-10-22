import random
import time

board = 10 * ["#"]

def display_board(board):
    blankBoard="""
___________________
|     |     |     |
|  7  |  8  |  9  |
|     |     |     |
|-----------------|
|     |     |     |
|  4  |  5  |  6  |
|     |     |     |
|-----------------|
|     |     |     |
|  1  |  2  |  3  |
|     |     |     |
|-----------------|
"""
    for i in range(1, 10):
        if board[i] == "#":
            blankBoard = blankBoard.replace(str(i), " ")
        else:
            blankBoard = blankBoard.replace(str(i), board[i])

    print(blankBoard)

def player_choice():
    while True:
        choice = input("Wprowadź czy grasz X czy O:")
        if choice.upper() == 'X':
            player1 = choice.upper()
            player2 = 'O'
            return player1, player2
            break
        elif choice.upper() == 'O':
            player1 = choice.upper()
            player2 = 'X'
            return player1, player2
            break
        else:
            continue

def player_place():
    if i % 2 != 0:
        place = int(input('Wprowadź pozycje na planszy:'))
        while True:
            if place > 0 and place < 10 and board[place] == "#":
                board[int(place)] = marker
                break
            else:
                place = int(input("Wprowadź poprawną pozycję:"))

    else:
        time.sleep(2)
        while True:
            place = random.randint(1, 9)
            if board[place] == "#":
                board[int(place)] = marker
                break


def win_check(board):
    if board[1] == board[2] == board[3] == players[0]:
        return True
    if board[4] == board[5] == board[6] == players[0]:
        return True
    if board[7] == board[8] == board[9] == players[0]:
        return True
    if board[1] == board[4] == board[7] == players[0]:
        return True
    if board[2] == board[5] == board[8] == players[0]:
        return True
    if board[3] == board[6] == board[9] == players[0]:
        return True
    if board[1] == board[5] == board[9] == players[0]:
        return True
    if board[3] == board[5] == board[7] == players[0]:
        return True
    if board[1] == board[2] == board[3] == players[1]:
        return 3
    if board[4] == board[5] == board[6] == players[1]:
        return 3
    if board[7] == board[8] == board[9] == players[1]:
        return 3
    if board[1] == board[4] == board[7] == players[1]:
        return 3
    if board[2] == board[5] == board[8] == players[1]:
        return 3
    if board[3] == board[6] == board[9] == players[1]:
        return 3
    if board[1] == board[5] == board[9] == players[1]:
        return 3
    if board[3] == board[5] == board[7] == players[1]:
        return 3
    return False

def full_board_check():
    if len([x for x in board if x == '#']) == 1:
        return True
    else:
        return False

def end():
    answer = input("Czy chcesz zagrać jeszcze raz? y/n:")
    while True:
        if answer.upper() == "Y":
            return True
            break
        elif answer.upper() == "N":
            return False
            break
        else:
            answer = input("Czy chcesz zagrać jeszcze raz? Wprowadź y/n:")




#player_choice()
players = player_choice()
display_board(board)
i = 0
z = 1

while True:
    if i % 2 == 0:
        marker = players[0]
        i += 1
    else:
        marker = players[1]
        i += 1


    player_place()
    display_board(board)
    if win_check(board) == True:
        print("Gratulacje wygrałeś !")
        if end() == True:
            players = player_choice()
            i = 0
            board = 10 * ["#"]
            continue
        else:
            print("Dzięki za grę, do zobaczenia!")
            break

    if win_check(board) == 3:
        print("Komputer wygrał!")
        if end() == True:
            players = player_choice()
            i = 0
            board = 10 * ["#"]
            continue
        else:
            print("Dzięki za grę, do zobaczenia!")
            break

    if full_board_check() == True:
        print("Plansza jest pełna koniec gry !")
        if end() == True:
            players = player_choice()
            i = 0
            board = 10 * ["#"]
            continue
        else:
            print("Dzięki za grę, do zobaczenia!")
            break