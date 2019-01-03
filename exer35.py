"""
In the previous exercise we saved information about famous scientists names and birthdays to disk.
In this exercise, load that JSON file from disk, extract the months of all the birthdays,
and count how many scientists have a birthday in each month.

Your program should output something like:

{
	"May": 3,
	"November": 2,
	"December": 1
}
"""
from collections import Counter
import json

monthdict = {1:'January', 2:'February', 3:'March', 4:'April', 5:'May', 6:'June',
             7:'July', 8:'August', 9:'September', 10:'October', 11:'November',
			 12:'December'}


def get_json_data(file_name):
	with open(file_name,"r") as f:
	    data = json.load(f)
	return data

def month_names(data):
	dates = []
	for name in data:
	    dates.append(data[name])
	months =[]
	for item in dates:
		months.append(int(item[5:6]))
	final =[]
	for i in months:
		final.append(monthdict.get(i))

	c = Counter(final)
	return c 

if __name__ == '__main__':
	# file_name = raw_input('Please enter the file name that you want to get the data from:\n=>')
	# 'exer34.json' is the file name that i'm using
	month_names(get_json_data('exer34.json'))
