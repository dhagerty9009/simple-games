# Tic-tac-toe game, written by David Hagerty
# Licenced under the GPL, Copyright 2011
# The goal of tic-tac-toe is to get three of your letter in a row, either
# vertically, horizontally or diagonally

# Imports
import random

def drawBoard(board):
	# Draws the board, a list of 10 strings (list index [0] is ignored),
    # This will be refactored for the beta release to fit the formatting of the
    # other games
	print("   |   |")
	print(" "+board[7]+" | "+board[8]+" | "+board[9])
	print("   |   |")
	print("-----------")
	print("   |   |")
	print(" "+board[4]+" | "+board[5]+" | "+board[6])
	print("   |   |")
	print("-----------")
	print("   |   |")
	print(" "+board[1]+" | "+board[2]+" | "+board[3])
	print("   |   |")

def inputPlayerLetter():
	# Lets the player choose their letter
	# Returns a list where the first index is the player's letter, second is the computer's
	letter=""
	while not (letter=="X" or letter=="O"):
		letter=input("Do you want to be X or O? ").upper()
	if letter=="X":
		return ["X","O"]
	else:
		return ["O","X"]

def whoGoesFirst():
	# Choose the first player based on a "random" choice
	if random.randint(0,1)==0:
		return "computer"
	else:
		return "player"

def playAgain():
	# Returns True if the player wants to play again
    # Any input starting with 'y' is valid
	print("Do you want to play again (yes or no)?")
	return input().lower().startswith("y")

# This writes the player's move to the board passed as an argument.
# The board can either be the duplicate board or the game board
def makeMove(board, letter, move):
	board[move]=letter

# This returns True if the player has won
def isWinner(bo, le):
	return ((bo[7]==le and bo[8]==le and bo[9]==le) or # Across top
	(bo[4]==le and bo[5]==le and bo[6]==le) or # Across middle
	(bo[1]==le and bo[2]==le and bo[3]==le) or # Across bottom
	(bo[7]==le and bo[4]==le and bo[1]==le) or # Down the left
	(bo[8]==le and bo[5]==le and bo[2]==le) or # Down the middle
	(bo[9]==le and bo[6]==le and bo[3]==le) or # Down the right
	(bo[7]==le and bo[5]==le and bo[3]==le) or # Diagonal, top left to bottom right
	(bo[9]==le and bo[5]==le and bo[1]==le)) # Diagonal, top right to bottom left

# Duplicates the board and returns the duplicate
def getBoardCopy(board):
	dupeBoard=[]
	for i in board:
		dupeBoard.append(i)
	return dupeBoard

# Returns True if the passed move is free
def isSpaceFree(board,move):
	return board[move]==" "

# Get the player's move
def getPlayerMove(board):
	move=" "
	while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board,int(move)):
		move=input("What is your move (1-9)? ")
	return int(move)

# Returns a valid move from the passed list on the passed board
# Returns None if there is no valid move
def chooseRandomMoveFromList(board,movesList):
	possibleMoves=[]
	for i in movesList:
		if isSpaceFree(board,i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None

# Given a board and the computer's letter, find the optimal move
def getComputerMove(board,computerLetter):
	if computerLetter=="X":
		playerLetter="O"
	else:
		playerLetter="X"
	# The AI is set up here
    # The AI code is set up in order of priority
    # This could be refactored into seperate functions for the beta release
	# This checks if the computer can win in the next move
	for i in range(1,10):
		copy=getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy,computerLetter):
				return i
	# Check if the player can win on their next move and block them
	for i in range(1,10):
		copy=getBoardCopy(board)
		if isSpaceFree(copy,i):
			makeMove(copy,playerLetter,i)
			if isWinner(copy,playerLetter):
				return i
	# Try to take the corners
	move=chooseRandomMoveFromList(board, [1,3,7,9])
	if move!=None:
		return move
	# Try to take the center
	if isSpaceFree(board,5):
		return 5
	# Move on one of the sides
	return chooseRandomMoveFromList(board,[2,4,6,8])

# Return True if every space on the board is full, otherwise return False
def isBoardFull(board):
	for i in range(1,10):
		if isSpaceFree(board,i):
			return False
	return True

# The main program
print("Welcome to Tic-Tac-Toe!")

while True:
	theBoard=[" "]*10
	playerLetter,computerLetter=inputPlayerLetter().
	turn=whoGoesFirst()
	print("The "+turn+" will go first.")
	gameIsPlaying=True
	while gameIsPlaying:
		if turn=="player":
			drawBoard(theBoard)
			move=getPlayerMove(theBoard)
			makeMove(theBoard,playerLetter,move)
			if isWinner(theBoard,playerLetter):
				drawBoard(theBoard)
				print("Congratulations! You win the game!")
				gameIsPlaying=False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print("The game is a tie!")
					break
				else:
					turn="computer"
		else:
            # The only other turn is the conputer's, so there is no need for
            # arguments to the else statement
			move=getComputerMove(theBoard,computerLetter)
			makeMove(theBoard,computerLetter,move)
			if isWinner(theBoard,computerLetter):
				drawBoard(theBoard)
				print("The computer has beaten you! You lose.")
				gameIsPlaying=False
			else:
				if isBoardFull(theBoard):
					drawBoard(theBoard)
					print("The game is a tie!")
					break
				else:
					turn="player"
	if not playAgain():
		break
