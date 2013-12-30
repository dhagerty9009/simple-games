# simple-games.checkers, written by David Hagerty
# Copyright 2011, licenced under the GPL
#
# The goal of Checkers (or draughts) is to eliminate all of your opponent's pieces.
# You can only move diagonally forward, unless the piece is a king, kings can also move backwards.
# You capture pieces by jumping over them, only if they are adjacent to the capturing piece.

# This is what the initial board will look like
#
#      A    B    C    D    E    F    G    H
#   +----+----+----+----+----+----+----+----+
# 1 | B  |    | B  |    | B  |    | B  |    |
#   +----+----+----+----+----+----+----+----+
# 2 |    | B  |    | B  |    | B  |    | B  |
#   +----+----+----+----+----+----+----+----+
# 3 | B  |    | B  |    | B  |    | B  |    |
#   +----+----+----+----+----+----+----+----+
# 4 |    |  . |    |  . |    |  . |    |  . |
#   +----+----+----+----+----+----+----+----+
# 5 | .  |    |  . |    |  . |    |  . |    |
#   +----+----+----+----+----+----+----+----+
# 6 |    | W  |    | W  |    | W  |    | W  |
#   +----+----+----+----+----+----+----+----+
# 7 | W  |    | W  |    | W  |    | W  |    |
#   +----+----+----+----+----+----+----+----+
# 8 |    | W  |    | W  |    | W  |    | W  |
#   +----+----+----+----+----+----+----+----+
#
# It is a little oblong to account for the possibility of kings, which will look like WK and BK
# for white and black, respectively.

# Imports
import random

# The player chooses their starting color.
# The lighter pieces go first.
def getPlayerColor():
    choice = ""
    while choice == "":
        print("What color do you want to play?")
        choice = input("Black (B)? Or White (W)? ")
        choice = choice[0].upper()
        if choice == "B":
            return choice
        elif choice == "W":
            return choice
        else:
            print("You must type either 'w' or 'b'. Try again.")
            choice = ""

def getComputerColor(player):
    if player == "W":
        computer = "B"
    elif player == "B":
        computer = "W"
    return computer

# The game board
def drawBoard(pieces):
    line = "  +----+----+----+----+----+----+----+----+"
    columns = "     A    B    C    D    E    F    G    H"
    print(columns)
    print(line)
    for i in range(0, 8):
        if i%2==0:
            print(str(i+1)+" |    | "+str(pieces[i][0])+" |    | "+str(pieces[i][1])+" |    | "+str(pieces[i][2])+" |    | "+str(pieces[i][3])+" | ")
            print(line)
        elif i%2==1:
            print(str(i+1)+" | "+str(pieces[i][0])+" |    | "+str(pieces[i][1])+" |    | "+str(pieces[i][2])+" |    | "+str(pieces[i][3])+" |    | ")
            print(line)

def checkWin(player, computer):
    computer_win, player_win = false
    if player == 0:
        computer_win = true
    elif computer == 0:
        player_win = true
    return player_win, computer_win

def getWin(player, computer):
    if player == true:
        print("You win!")
    elif computer == true:
        print("You lose...")


#
# Movement of the pieces: The pieces are moved by typing in a column letter
# and a row number for the piece you want to move, and then a column letter
# and a row number for the spot you want to move to. If that spot is occupied
# by an enemy piece, then your piece will be moved to the next open square in
# the path of movement.
#
#

# Here is the main game
print("Welcome to the game of checkers!")
print("Please choose your color.")
player_color = getPlayerColor()
print("You are playing as "+player_color)
computer_color = getComputerColor(player_color)
print("The computer is playing as "+computer_color)
player_pieces = 12
computer_pieces = 12
pieces_positions = [("B ", "B ", "B ", "B "), ("B ", "B ", "B ", "B "), ("B ", "B ", "B ", "B "), (". ", ". ", ". ", ". "), (". ", ". ", ". ", ". "), ("W ", "W ", "W ", "W "), ("W ", "W ", "W ", "W "), ("W ", "W ", "W ", "W ")]
print()
drawBoard(pieces_positions)
