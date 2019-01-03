"""
This exercise is Part 1 of 4 of the birthday data exercise series. The other exercises are: Part 2, Part 3, and Part 4.

For this exercise, we will keep track of when our friend's birthdays are,
and be able to find that information based on their name. Create a dictionary (in your file) of names and birthdays.
When you run your program it should ask the user to enter a name,
and return the birthday of that person back to them.
"""
birthdays = {'Mohamed Shili': '1996/06/09', 'Mr Alison': '1885/11/02', 'Jack Wilson': '1989/8/27'}

print 'Welcome to the birthday dictionary. We know the birthdays of:'
for i in birthdays:
    print '- ' + i
answer = raw_input('Which One You Wanna Check?:\n>> ')
try:
    print (birthdays[answer])
except KeyError:
    print 'We Could Not Find This Person Birthday In Our Data Base'
finally:
    print "\nThanks For Using Our Script\n"
