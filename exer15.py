""""
Write a program (using functions!) that asks the user for a long string containing multiple words.
Print back to the user the same string, except with the words in backwards order. For example, say I type the string:
"""

def str_reverser(input = None):
    if input != None:
        data = ' '.join(input.split()[::-1])
    else:
        data = raw_input('Please Enter any string you like\n=> ')
        data = ' '.join(data.split()[::-1])


    print (data)

if __name__ == '__main__':
    str_reverser()
