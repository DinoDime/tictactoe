import random

openSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
boardRows = 3
boardColumns = 3


def print_board():  # prints tic tac toe board
    for row in range(boardRows):
        print("\n+---+---+---+")
        print("|", end="")
        for col in range(boardColumns):
            print("", gameBoard[row][col], end=" |")
    print("\n+---+---+---+")


def record_turn(num, turn):  # records a user's turn choice
    num -= 1
    if num == 0:
        gameBoard[0][0] = turn
    elif num == 1:
        gameBoard[0][1] = turn
    elif num == 2:
        gameBoard[0][2] = turn
    elif num == 3:
        gameBoard[1][0] = turn
    elif num == 4:
        gameBoard[1][1] = turn
    if num == 5:
        gameBoard[1][2] = turn
    if num == 6:
        gameBoard[2][0] = turn
    if num == 7:
        gameBoard[2][1] = turn
    if num == 8:
        gameBoard[2][2] = turn


keepPlaying = True
turnTracker = 1  # human player takes odd turn


def choose_symbol():
    symbol = input("Please choose X or O: ").upper()
    while symbol != "X" or symbol != "O":
        symbol = input("Sorry, that entry was invalid. Please try again. \nPlease choose X or O: ").upper()
    if symbol == "X":
        computer_symbol = "O"
    else:
        computer_symbol = "X"


def play_game(symbol):
    while keepPlaying:
        if not openSpaces:
            break
        if turnTracker % 2 == 1:
            print_board()
            spot_picked = int(input("\nChoose a position on the board, 1 - 9: "))
            if spot_picked >= 1 or spot_picked <= 9:
                record_turn(spot_picked, symbol)
                openSpaces.remove(spot_picked)
            else:
                print("Sorry, that was an invalid entry. Please try again.")
                continue
