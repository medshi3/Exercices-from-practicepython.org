from exer26 import *

game = [[0, 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]

def player1():
	play = raw_input('You are "X" what would you play\n\n>>> ')
	x = int(play[0])
	y = int(play[2])
	if game[x][y] == 0:
		game[x][y] = 'X'
		counter.append(1)
	else :
		print 'You can do this move is hold by {}'.format(game[x][y])
		player1()

def player2():
	play2 = raw_input('You are "O" what would you play\n\n>>> ')
	x = int(play2[0])
	y = int(play2[2])
	if game[x][y] == 0:
		game[x][y] = 'O'
		counter.append(1)
	else :
		print 'You can do this move is hold by {}'.format(game[x][y])
		player2()

counter = []
runing = True
while runing:
	if len(counter) == 9 and is_win(game) == None:
		print "the game has end, There is No Winner !"
		runing = False
	if len(counter) <9 and is_win(game) == None:
			player1()
	else:
		print (is_win(game) + "the Game has end")
		runing = False

	if len(counter) <9 and is_win(game) == None:
		player2()
