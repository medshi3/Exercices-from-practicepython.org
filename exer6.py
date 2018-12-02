"""
    Ask the user for a string and print out whether this string is a palindrome or not.
    (A palindrome is a string that reads the same forwards and backwards.)
"""
data = raw_input('Please enter any string you like \n=> ')

if data[::-1] == data:
    print "Your string '{}' is a palindrome".format(data)
else:
    print "Your string '{}' is not a palindrome".format(data)
