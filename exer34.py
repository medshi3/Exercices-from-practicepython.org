"""
In this exercise, modify your program from Part 1 to load the birthday dictionary from a JSON file on disk,
rather than having the dictionary defined in the program.

Bonus: Ask the user for another scientist's name and birthday to add to the dictionary,
and update the JSON file you have on disk with the scientis's name.
If you run the program multiple times and keep adding new names, your JSON file should keep getting bigger and bigger.
"""
# Importing the Module
import json
# This is the data that we will write in the json file
birthdays = {'Mohamed Shili': '1996/6/09', 'Mr Alison': '1885/11/02', 'Jack Wilson': '1989/8/27',
             'Jacky': '1898/6/25', 'Sandra Adison': '1952/11/15', 'Mark Stark': '1975/8/18'}

# this will open the file and write in it (if the file does not exist it will creat it)
with open("exer34.json", "w") as f:
    json.dump(birthdays, f)
# we close the file to open it in another mode
f.close()

# we open the file again in read mode to load the data
with open("exer34.json", "r") as f:
    birthdayss = json.load(f)

print 'Welcome to the birthday dictionary. We know the birthdays of:'
for i in birthdayss:
    print '- ' + i
answer = raw_input('Which One You Wanna Check?:\n>> ')
try:
    print (birthdayss[answer])
except KeyError:
    print 'We Could Not Find This Person Birthday In Our Data Base'
finally:
    print "\nThanks For Using Our Script\n"
