"""Generate a random number between 1 and 9 (including 1 and 9).
Ask the user to guess the number, then tell them whether they guessed too low, too high, or exactly right
"""
from random import randint

while True:
    n = randint(1,9)
    print "The computer just picked a number between 1-9!\n"

    num = int(raw_input('Please Enter a guess Number '))

    if n == num:
        print " You guess it! exactly right {} is the number".format(n)
    elif n > num and (n - num) == 1:
        print "Your guess is too high! the number is {}".format(n)
    elif  n < num and (num - n) == 1:
        print "Your guess is too high! the number is {}".format(n)
    else :
        print "Your guess is too low! the number is {}".format(n)
