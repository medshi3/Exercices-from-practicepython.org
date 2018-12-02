"""Create a program that asks the user to enter their name and their age.
Print out a message addressed to them that tells them the year that they will turn 100 years old.
"""

import datetime
now = datetime.datetime.now()

name = raw_input('please enter your name\n=> ')
age = int(raw_input('Please enter your age\n=> '))
diff = 100 - int(age)
turno = (now.year - age) + 100
print "So your name is {}, {} years old and you will turn 100 on {}".format(name, age, turno)
