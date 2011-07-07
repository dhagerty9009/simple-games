# simple-games.checkers, written by David Hagerty
# Copyright 2011, licenced under the GPL
#
# The goal of Checkers (or draughts) is to eliminate all of your opponent's pieces.
# You can only move diagonally forward, unless the piece is a king, kings can also move backwards.
# You capture pieces by jumping over them, only if they are adjacent to the capturing piece.

# This is what the initial board will look like
#
#     A   B   C   D   E   F   G   H
#   +---+---+---+---+---+---+---+---+
#   | B |   | B |   | B |   | B |   |
#   +---+---+---+---+---+---+---+---+
#   |   | B |   | B |   | B |   | B |
#   +---+---+---+---+---+---+---+---+
#   | B |   | B |   | B |   | B |   |
#   +---+---+---+---+---+---+---+---+
#   |   | . |   | . |   | . |   | . |
#   +---+---+---+---+---+---+---+---+
#   | . |   | . |   | . |   | . |   |
#   +---+---+---+---+---+---+---+---+
#   |   | W |   | W |   | W |   | W |
#   +---+---+---+---+---+---+---+---+
#   | W |   | W |   | W |   | W |   |
#   +---+---+---+---+---+---+---+---+
#   |   | W |   | W |   | W |   | W |
#   +---+---+---+---+---+---+---+---+

# Imports
import random

# The player chooses their starting color.
# The lighter pieces go first.
def getPlayerColor():
    choice = ""
    while choice != "B" or choice != "W":
        print("What color do you want to play?")
        choice = input("Black (B)? Or White (W)?")
        choice = choice[0].upper()
        if choice == "B":
            unchosen = "W"
            break
        elif choice == "W":
            unchosen = "B"
            break
        else:
            print("Invalid option, try again.")
    return choice, unchosen

# The game board
def drawBoard():
    line = " +---+---+---+---+---+---+---+---+"
    collumns = "   A   B   C   D   E   F   G   H"
    print(collumns)
    print(line)
#
# Movement of the pieces: The pieces are moved by typing in a collumn letter
# and a row number for the piece you want to move, and then a collunm letter
# and a row number for the spot you want to move to. If that spot is occupied
# by an enemy piece, then your piece will be moved to the next open square in
# the path of movement.
#
#

# Here is the main game
print("Welcome to the game of checkers!")
print("Please choose your color.")
player, computer = getPlayerColor()
print("You are playing as "+player)
print("The computer is playing as "+computer)
print()
drawBoard()
