"""
Write a program that takes a list of numbers
(for example, a = [5, 10, 15, 20, 25]) and makes a new list of only the first and last elements of the given list.
For practice, write this code inside a function.
"""
from re import findall

def first_last_num():
    data = raw_input('please enter a list of number!\nfor example:\n\t [1, 2, 5]\n\n => ')
    num = findall(r'[\d]+', data)

    print "Here is the last and the first number of your list ({}, {})".format(num[0], num[-1])

if __name__ == '__main__':
    first_last_num()
