"""Ask the user for a number and determine whether the number is prime or not.
(For those who have forgotten, a prime number is a number that has no divisors.)
"""

def prime_or_not():
    num = int(raw_input('Please enter any number \n=> '))

    if num % 2 == 1:
        print "{} its  a prime number".format(num)
    else:
        print "{} its not a prime number".format(num)

if __name__ == '__main__':
    prime_or_not()
