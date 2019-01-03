# The list of the Game | its 3 * 3
game = [['X', 0, 0],
	   [0, 0, 0],
	   [0, 0, 0]]

def draw(l):

    n = len(l)

    symbole =  {'dot' :' ---', 'pipe' :'|   '}
    pipe ='|   '
    c = n * symbole['dot']
    d = (n+1) * symbole['pipe']

    for i in range(0,n):
        print c
        print d
        print c
if __name__ == '__main__':
    draw(game)
