"""
    Implement a function that takes as input three variables, and returns the largest of the three.
    Do this without using the Python max() function!

    The goal of this exercise is to think about some internals that Python normally takes care of for us.
    All you need is some variables and if statements!
"""
from random import randint
def max_var(a, b, c):
    nums = [i for i in a,b,c]
    nums.sort()
    print "Here is ur numbers: {}, {}, {}".format(a,b,c)
    return "here is ur largest number: {}".format(nums[-1])


if __name__ == '__main__':
    max_var(randint(0,100), randint(0,100), randint(0,100))
