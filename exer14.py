"""
Write a program (function!)
that takes a list and returns a new list that contains all the elements of the first list minus all the duplicates.
Write two different functions to do this - one using a loop and constructing a list, and another using sets.
"""

from re import findall

def non_duplicated(data):
    new_list = []
    for i in data:
        if i not in new_list:
            new_list.append(i)

    print new_list
def get_list():
    data = raw_input('please enter a list of number!\nfor example:\n\t [1, 2, 5]\n\n => ')
    num = findall(r'[\w]+|[\d]+', data)
    non_duplicated(num)

if __name__ == '__main__':
    get_list()
