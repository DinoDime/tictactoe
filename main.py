import random

boardSpaces = [1, 2, 3, 4, 5, 6, 7, 8, 9]
gameBoard = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
boardRows = 3
boardColumns = 3


def print_board():
    for row in range(boardRows):
        print("\n+---+---+---+")
        print("|", end="")
        for col in range(boardColumns):
            print("", gameBoard[row][col], end=" |")
    print("\n+---+---+---+")

print_board()
