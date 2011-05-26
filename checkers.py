# simple-games.checkers, written by David Hagerty
# Copyright 2011, licenced under the GPL
#
# The goal of Checkers (or draughts) is to eliminate all of your opponent's pieces.
# You can only move diagonally forward, unless the piece is a king, kings can also move backwards.
# You capture pieces by jumping over them, only if they are adjacent to the capturing piece.

# This is what the initial board will look like
#
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

# Here is the main game
print("Welcome to the game of checkers!")
print("Please choose your color.")
player, computer = getPlayerColor()
print("You are playing as "+player)
print("The computer is playing as "+computer)
