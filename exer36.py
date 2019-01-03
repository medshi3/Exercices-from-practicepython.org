"""
This exercise is Part 4 of 4 of the birthday data exercise series. The other exercises are: Part 1, Part 2, and Part 3.
In the previous exercise we counted how many birthdays there are in each month in our dictionary of birthdays.
In this exercise, use the bokeh Python library to plot a histogram of which months the scientists have birthdays in!
Because it would take a long time for you to input the months of various scientists, you can use my scientist birthday JSON file.
Just parse out the months and draw your histogram.

example of using bokeh
from bokeh.plotting import figure, show, output_file
output_file('plot.html')
x = [10,20,30]
y = [4,5,6]
p = figure()
p.vbar(x=x, top=y, wifth = 0.5)

"""
from bokeh.plotting import figure, show, output_file
from exer35 import *

data = month_names(get_json_data('exer34.json'))

# we specify an HTML file where the output will go
output_file("months.html")

# load our x and y data
x_categories = list(data.keys())
x = [i for i in data]
y = [data[i] for i in x]

# create a figure
p = figure()
p = figure(x_range=x_categories)

# create a histogram
p.vbar(x=x, top=y, width = 0.5)

# render (show) the plot
show(p)
