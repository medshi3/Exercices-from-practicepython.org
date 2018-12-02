"""
Write a password generator in Python. Be creative with how you generate passwords - strong passwords have a mix of lowercase letters,
uppercase letters, numbers, and symbols. The passwords should be random,
generating a new password every time the user asks for a new password. Include your run-time code in a main method.

Extra:

    Ask the user how strong they want their password to be. For weak passwords, pick a word or two from a list.
"""
import random
# abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ !"#$%&'()*+,-./:;<=>?@[\]^_`{|}~

def pass_generator():
    # Assking for inforamtion from the user
    pick = raw_input('What level of Password you like:\n\t-high\n\t-medium\n\t-low\n\t=> ')
    n = int(raw_input('How long you want your Password:\n=> '))
    levels = {
    'high':{1:' !"#$%&\'()*+,-./:;<=>?@[\]^_`{|}~',2: 'abcdefghijklmnopqrstuvwxyz', 3:'ABCDEFGHIJKLMNOPQRSTUVWXYZ',4:'123456789' },
    'medium':{1: 'abcdefghijklmnopqrstuvwxyz', 2:'ABCDEFGHIJKLMNOPQRSTUVWXYZ',3:'123456789'},
    'low':{1: 'abcdefghijklmnopqrstuvwxyz', 2:'123456789'}
    }

    caracters = []

    for i in range(0,n):
        if pick == 'high':
            caracters.append(random.choice(levels[pick][random.randint(1,4)]))
        elif pick == 'medium':
                caracters.append(random.choice(levels[pick][random.randint(1,3)]))
        else:
            caracters.append(random.choice(levels[pick][random.randint(1,2)]))
    new_pass = ''.join(caracters)
    print(new_pass)

if __name__ == '__main__':
    pass_generator()
