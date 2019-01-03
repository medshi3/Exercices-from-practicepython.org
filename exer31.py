"""
An example interaction can look like this:

>>> Welcome to Hangman!
_ _ _ _ _ _ _ _ _
>>> Guess your letter: S
Incorrect!
>>> Guess your letter: E
E _ _ _ _ _ _ _ E

Let's say the word the player has to guess is "EVAPORATE". For this exercise,
write the logic that asks a player to guess a letter and displays letters in the clue word that were guessed correctly.
For now, let the player guess an infinite number of times until they get the entire word. As a bonus
keep track of the letters the player guessed and display a different message if the player tries to guess that letter again.
Remember to stop the game when all the letters have been guessed correctly!
Don't worry about choosing a word randomly or keeping track of the number of guesses the player has remaining -
we will deal with those in a future exercise.
"""
from exer30 import *
def hangman(word):
    word = list(word)
    letter =[i for i in word[0]]
    guessed = "_" * len(letter)
    guessed = list(guessed)
    lstGuessed = []
    ans = []
    Try = 0
    print "Welcome To Hangman Game! :D \n The word has {} caracter,one of them is {}".format(len(letter), random.choice(letter))
    print(' '.join(guessed))
    while True:
        answer = raw_input('\nPlease Pick a Letter:\n\t>>> ')
        if answer.upper() in letter:
            index = letter.index(answer.upper())
            guessed[index] = answer.upper()
            letter[index] = '_'
            lstGuessed.append(answer.upper())
            print(' '.join(guessed))
        elif answer.upper() in lstGuessed:
            print "You have already guesses this letter!\n"
            print "\nYou Got {} Try's Left X(".format(5-Try)
            print(' '.join(guessed))
            Try += 1
        else :
            lstGuessed.append(answer.upper())
            print "\n=> Wrong Letter!\n"
            print "\nYou Got {} Try's Left X(".format(5-Try)
            print(' '.join(guessed))
            Try += 1
        if Try == 6:
            print "\nSorry but You lost!\nMore then 6 Try's"

            playAgain()
            break

        if '_' not in guessed:
            print("\nYou Won!!")
            playAgain()
            break
# this function ask if the player wanna play again or exit
def playAgain():
    play = raw_input('Wanna Play again ?\n>>> ')
    if play.lower() == 'yes':
        hangman(word_gen())
    else:
        print "Okay Thanks for Playing losser :D"
