"""
make board
ask user where they want to make their move
ask user if they want to play against a
human or computer
check for winner/tie
print board
iterate
"""
import random
board = [
    ["[1]", "[2]", "[3]"]
    ["[4]", "[5]", "[6]"]
    ["[7]", "[8]", "[9]"]
]

def check_for_win(board):

def gameplay():
    print("Welcome to Tic Tac Toe!")
    player_symbol = input("Would you like to be X or O?").upper()
    while player_symbol != "X" or player_symbol != "O":
        player_symbol = input("Please try again. You must choose X or O.").upper()
    

