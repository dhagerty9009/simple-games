#tic-tac-toe game
import random
def drawBoard(board):
	#this draws the board
	#board is a list of 10 strings (list index [0] is ignored)
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
	#lets the player choose their letter
	#returns a list where the first index is the player's letter, second is the computer's
	letter=""
	while not (letter=="X" or letter=="O"):
		letter=input("Do you want to be X or O? ").upper()
	if letter=="X":
		return ["X","O"]
	else:
		return ["O","X"]
def whoGoesFirst():
	#choose the first player based on a "random" choice
	if random.randint(0,1)==0:
		return "computer"
	else:
		return "player"
def playAgain():
	#returns True if the player wants to play again
	print("Do you want to play again (yes or no)?")
	return input().lower().startswith("y")
def makeMove(board, letter, move):
	board[move]=letter
def isWinner(bo, le):
	#this returns True if the player has won
	return ((bo[7]==le and bo[8]==le and bo[9]==le) or #across top
	(bo[4]==le and bo[5]==le and bo[6]==le) or #across middle
	(bo[1]==le and bo[2]==le and bo[3]==le) or #across bottom
	(bo[7]==le and bo[4]==le and bo[1]==le) or #down the left
	(bo[8]==le and bo[5]==le and bo[2]==le) or #down the middle
	(bo[9]==le and bo[6]==le and bo[3]==le) or #down the right
	(bo[7]==le and bo[5]==le and bo[3]==le) or #diagonal, top left to bottom right
	(bo[9]==le and bo[5]==le and bo[1]==le)) #diagonal, top right to bottom left
def getBoardCopy(board):
	#duplicate the board list and return the duplicate
	dupeBoard=[]
	for i in board:
		dupeBoard.append(i)
	return dupeBoard
def isSpaceFree(board,move):
	#returns True if the passed move is free
	return board[move]==" "
def getPlayerMove(board):
	#get the player's move
	move=" "
	while move not in "1 2 3 4 5 6 7 8 9".split() or not isSpaceFree(board,int(move)):
		move=input("What is your move (1-9)? ")
	return int(move)
def chooseRandomMoveFromList(board,movesList):
	#returns a valid move from the passed list on the passed board
	#returns None if there is no valid move
	possibleMoves=[]
	for i in movesList:
		if isSpaceFree(board,i):
			possibleMoves.append(i)
	if len(possibleMoves) != 0:
		return random.choice(possibleMoves)
	else:
		return None
def getComputerMove(board,computerLetter):
	#given a board and the computer's letter, find the optimal move
	if computerLetter=="X":
		playerLetter="O"
	else:
		playerLetter="X"
	#the AI is set up here
	#this checks if the computer can win in the next move
	for i in range(1,10):
		copy=getBoardCopy(board)
		if isSpaceFree(copy, i):
			makeMove(copy, computerLetter, i)
			if isWinner(copy,computerLetter):
				return i
	#check if the player can win on their next move and block them
	for i in range(1,10):
		copy=getBoardCopy(board)
		if isSpaceFree(copy,i):
			makeMove(copy,playerLetter,i)
			if isWinner(copy,playerLetter):
				return i
	#try to take the corners
	move=chooseRandomMoveFromList(board, [1,3,7,9])
	if move!=None:
		return move
	#try to take the center
	if isSpaceFree(board,5):
		return 5
	#move on one of the sides
	return chooseRandomMoveFromList(board,[2,4,6,8])
def isBoardFull(board):
	#return True if every space on the board is full, otherwise return False
	for i in range(1,10):
		if isSpaceFree(board,i):
			return False
	return True
print("Welcome to Tic-Tac-Toe!")

while True:
	#resets the board
	theBoard=[" "]*10
	playerLetter,computerLetter=inputPlayerLetter().
	turn=whoGoesFirst()
	print("The "+turn+" will go first.")
	gameIsPlaying=True
	while gameIsPlaying:
		if turn=="player":
			#player's turn
			drawBoard(theBoard)
			move=getPlayerMove(theBoard)
			makeMove(theBoard,playerLetter,move)
			#check if this move ends the game
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
			#computer's turn
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
