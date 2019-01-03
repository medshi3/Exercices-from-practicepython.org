"""
Given two .txt files that have lists of numbers in them,
find the numbers that are overlapping. One .txt file has a list of all prime numbers under 1000,
and the other .txt file has a list of happy numbers up to 1000.

(If you forgot, prime numbers are numbers that can't be divided by any other number.
And yes, happy numbers are a real thing in mathematics - you can look it up on Wikipedia.
The explanation is easier with an example, which I will describe below.)
"""

def file_to_list(f1, f2):
    pr_list = []
    hp_list = []
    # read data from file 1 and append to a list
    lines1 = f1.readlines()
    for line in lines1:
        pr_list.append(int(line))
    # read data from file 2 and append to a list
    lines2 = f2.readlines()
    for line in lines2:
        hp_list.append(int(line))
    # put the overlapping num in a list
    overlapping_num= [i for i in pr_list if i in hp_list]
    print overlapping_num

# Open the two files and pass them to a function
with open('prime_num.txt', 'r') as pr, open('happy_num.txt') as hp:
    file_to_list(pr, hp)
