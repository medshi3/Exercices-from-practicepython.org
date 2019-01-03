
def check_win(l):
    for x in range(0,2):

    # Vertical winner
        if (l[0][x] ==  l[1][x] ==  l[2][x]) and l[0][x] != 0:
            return l[0][x]
        # Horizental winner
        elif (l[x][0] ==  l[x][1] ==  l[x][2])  and l[x][0] != 0:
            return l[x][0]
        # Diagonal winner
        if (l[0][0] ==  l[1][1] ==  l[2][2] or  l[0][2] ==  l[1][1] ==  l[2][0]) and l[1][1] != 0:
            return l[1][1]
        else:
            return None

def is_win(l):
    win = check_win(l)
    if win == 'X':
        return "Player 1 Win!"
    elif win == 'O':
        return "Player 2 Win!"
    else:
        return None





"""game = [[1, 2, 0],
	    [2, 1, 0],
	    [2, 1, 1]]

winner_is_2 = [[2, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_1 = [[1, 2, 0],
	           [2, 1, 0],
	           [2, 1, 1]]

winner_is_also_1= [[0, 1, 0],
	                [2, 1, 0],
	                [2, 1, 1]]

no_winner = [[1, 2, 0],
	         [2, 1, 0],
	         [2, 1, 2]]

also_no_winner = [[1, 2, 0],
	              [2, 1, 0],
	              [2, 1, 0]]
"""
