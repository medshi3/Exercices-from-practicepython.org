"""
Create a program that will play the "cows and bulls" game with the user. The game works like this:
Randomly generate a 4-digit number. Ask the user to guess a 4-digit number.
For every digit that the user guessed correctly in the correct place, they have a "cow".
For every digit the user guessed correctly in the wrong place is a "bull." Every time the user makes a guess,
tell them how many "cows" and "bulls" they have. Once the user guesses the correct number, the game is over.
Keep track of the number of guesses the user makes throughout teh game and tell the user at the end.
"""
# import the randint function from the random module to generate a random 4 digits
from random import randint

print "Welcome to the Cows and Bulls Game!"
# make a list of the 4-digits number
var_list = [i for i in str(randint(1000,9999))]

# infinit loop till its true to break
while True:
    # a list of the 4-digits number of the user
    answer_list = [i for i in raw_input("Please Enter a 4-digit number:\n=>")]
    # check if any commen numbers between the user input and the random digits
    commen_list = [i for i in answer_list if i in var_list]
    bulls = []
    cow = []
    # a loop depend if any commen digits
    for i in range(0,len(commen_list)):
        # if they are in the same place thats a Bull
        if commen_list[i] == var_list[i]:
            bulls.append(i)
        # if they are not in the same place thats a cow
        elif commen_list[i] != var_list[i]:
            cow.append(i)
    print "You got {} bulls".format(len(bulls))
    print "You got {} cow".format(len(cow))

    # if we got 4 digits in the Bull list thats a Win!
    if len(bulls) == 4:
        print "You win! :D"
        break
