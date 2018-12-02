"""
    Make a two-player Rock-Paper-Scissors game. (Hint: Ask for player plays (using input)
    compare them, print out a message of congratulations to the winner, and ask if the players want to start a new game)

Remember the rules:

    Rock beats scissors
    Scissors beats paper
    Paper beats rock
"""

from random import randint



def game():
    try:
        player = int(raw_input("Please enter a number\n\t1-Rock\n\t2-Scissors\n\t3-Paper\n\t=> "))
    except ValueError:
        print "enter a number please"
    picks = {1:'Rock', 2:'Scissors', 3:'Paper'}
    random_pick = randint(1,3)
    if random_pick > player:
        return "You lose! {} cant beat What computer picked {}".format(picks[player], picks[random_pick])
    elif player == random_pick:
        return "No one wins ! {} cant beat What computer picked {}".format(picks[player], picks[random_pick])
    else:
        return "You Win! {} cant beat What computer picked {}".format(picks[player], picks[random_pick])


if __name__ == '__main__':
    game()
