# Written by David Hagerty, licenced under GPL 2011
# This is Reversi, or Othello
# The goal in this game is to cover as much of the board as possible with your pieces, and get rid of your opponents pieces.

# Imports
import random
import sys

# The player chooses their tile color
def getPlayerTile():
	tile=" "
	while not(tile=="B" or tile=="W"):
		print("Do you want to be black or white (B or W)?")
		tile=input().upper()
	if tile=="B":
		return ["B","W"]
	else:
		return ["W","B"]

# Black always goes first, so a function choosing who goes first is not needed

# This function draws the board to the screen
def drawBoard(board):
	HLINE="+---+---+---+---+---+---+---+---+"
	VLINE="|   |   |   |   |   |   |   |   |"
	print("  1   2   3   4   5   6   7   8")
	for y in range(8):
		print(VLINE)
		print(y+1, end=" ")
		for x in range(8):
			print("| %s" % board[x][y], end=" ")
		print("|")
		print(VLINE)
		print(HLINE)

# Creates an 8x8 array used for the board
def makeNewBoard():
	board=[]
	for i in range(8):
		board.append(" "*8)
	return board

# Sets the starting pieces for a new game
def resetBoard(board):
	for x in range(8):
		for y in range(8):
			board[x][y]=" "
	board[4][4]="B"
	board[4][5]="W"
	board[5][4]="W"
	board[5][5]="B"

# This function gets the player's move for the turn
# Moves are taken as a two-digit integer with the x-value as the first digit and the y-value as the second digit
def getPlayerMove(board,playerTile):
	digits1to8="1 2 3 4 5 6 7 8".split()
	while True:
		print("Enter your move, type 'hints' to turn hints on/off, or type 'quit' to quit.")
		move=input().lower()
		if move==quit:
			return "quit"
		if move==hints:
			return "hints"
		if len(move)==2 and move[0] in digits1to8 and move[1] in digits1to8:
			x=int(move[0]-1) # Arrays are indexed @ 0, so the actual index is one less than the user's input
			y=int(move[1]-1)
			if isValidMove(board,tile,x,y)==False:
				continue
			else:
				break
		else:
			print("That is not a valid move. Type in the x digit (1-8), and then the y digit (1-8)")
			print("For example, 81 would be the top right corner")
	return [x,y]

# Checks the validity of any moves made by the players (user and computer)
def isValidMove(board,tile,xstart,ystart):
	if board[xstart][ystart] != " " or not isOnBoard(xstart,ystart):
		return False
	board[xstart][ystart]=tile
	if tile=="X":
		otherTile="O"
	else:
		otherTile="X"
	tilesToFlip=[]
	for xdirection,ydirection in [[-1,0],[-1,-1],[0,-1],[0,0],[1,0],[1,1],[0,1],[-1,1],[1,-1]]:
		x,y=xstart,ystart
		x+=xdirection
		y+=ydirection
		if isOnBoard(x,y) and board[x][y]==otherTile:
			x+=xdirection
			y+=ydirection
				if not isOnBoard(x,y):
				continue
			while board[x][y]==otherTile:
				x+=xdirection
				y+=ydirection
				if not isOnBoard(x,y):
					break
			if not isOnBoard(x,y):
				continue
			if board[x][y]==tile:
				while True:
					x-=xdirection
					y-=ydirection
					if x==xstart and y==ystart:
						break
					tilesToFlip.append([x,y])
	board[xstart][ystart]=" "
	if len(tilesToFlip)==0:
		return False
	else:
		return tilesToFlip

# Creates a board with valid moves marked by '.'
def getBoardWithValidMoves(board,tile):
	dupeBoard=getBoardCopy(board)
	for x,y in getValidMoves(dupeBoard,tile):
		dupeBoard[x][y]="."
	return dupeBaord

# Finds all valid moves for player
def getValidMoves(board,tile):
	validMoves=[]
	for x in range(8):
		for y in range(8):
			if isValidMove(board,tile,x,y)!=False:
				validMoves.append([x,y])
	return validMoves

# Finds the score of the game
def getScoreOfBoard(board):
	Bscore=0
	Wscore=0
	for x in range(8):
		for y in range(8):
			if board[x][y]=="B"
				Bscore+=1
			if board[x][y]=="W"
				Wscore+=1
	return {"B":Bscore,"W":Wscore}

# Asks the user if they want to play again, any input starting with 'y' is valid
def playAgain():
	print("Do you want to play again (yes or no)?")
	return input().lower().startswith("y")

# Writes the player's or computer's move to the board
def makeMove(board,tile,xstart,ystart):
	tilesToFlip=isValidMove(board,tile,xstart,ystart)
	if tilesToFlip==False:
		return False
	board[xstart][ystart]=tile
	for x,y in tilesToFlip:
		board[x][y]=tile
	return True

# Copies the game board to validate moves
def getBoardCopy(board):
	dupeBoard=makeNewBoard()
	for x in range(8):
		for y in range(8):
			dupeBoard[x][y]=board[x][y]
	return dupeBoard

# Checks if a tile is on a corner
def isOnCorner(x,y):
	return (x==0 and y==0) or (x==7 and y==0) or (x==0 and y==7) or (x==7 and y==7)

# Gets the computer's move based on best score, i.e. most tiles the move will flip
def getComputerMove(board,computerTile):
	possibleMoves=getValidMoves(board,computerTile)
	random.shuffle(possibleMoves)
	for x,y in possibleMoves:
		if isOnCorner(x,y):
			return [x,y]
	bestScore=-1
	for x,y in possibleMoves:
		dupeBoard=getBoardCopy(board)
		makeMove(dupeBoard,computerTile,x,y)
		score=getScoreOfBoard(dupeBoard)[computerTile]
		if score>bestScore:
			bestMove=[x,y]
			bestScore=score
	return bestMove

# Shows the game's score
def showScore(playerTile,computerTile):
	scores=getScoreOfBoard(mainBoard)
	print("You have %s points. The computer has %s points." % (scores[playerTile] scores[computerTile]))

# The actual game, not all the logic
print("Welcome to Reversi!")
while True:
	mainBoard=makeNewBoard()
	resetBoard(mainBoard)
	playerTile, computerTile=getPlayerTile()
	showHints=False
	if playerTile=="B":
		turn="player"
	else:
		turn="computer"
	print("The "+turn+" will go first")
	while True:
		if turn=="player":
			if showHints:
				validMovesBoard=getBoardWithValidMoves(mainBoard,playerTile)
				drawBoard(validMovesBoard)
			else:
				drawBoard(mainBoard)
			showScore(playerTile,computerTile)
			move=getPlayerMove(mainBoard,playerTile)
			if move=="quit":
				print("Thanks for playing!")
				sys.exit()
			elif move=="hints":
				showHints=not showHints
				continue
			else:
				makeMove(mainBoard,playerTile,move[0],move[1])
			if getValidMoves(mainBoard,computerTile)==[]:
				break
			else:
				turn="computer"
		else:
			drawBoard(mainBoard)
			showScore(playerTile,computerTile)
			input("Press <Enter> to see the computer's move.")
			x,y=getComputerMove(mainBoard,computerTile)
			makeMove(mainBoard,computerTile,x,y)
			if getValidMoves(mainBoard,playerTile)==[]:
				break
			else:
				turn="player"
	drawBoard(mainBoard)
	scores=getScoreOfBoard(mainBoard)
	print("Black scored %s points. White scored %s points." % (scores["B"] scores["W"]))
	if scores[playerTile]>scores[computerTile]:
		print("You beat the computer by %s points!" % (scores[playerTile]-scores[computerTile]))
	elif scores[computerTile]>scores[playerTile]:
		print("The computer beat you by %s points!" % (scores[computerTile]-scores[playerTile]))
	else:
		print("The games is a tie!")
	if not playAgain:
		break
