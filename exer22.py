"""
    Given a .txt file that has a list of a bunch of names,
    count how many of each name there are in the file, and print out the results to the screen.
    I have a .txt file for you, if you want to use it!

    Extra:

    Instead of using the .txt file from above (or instead of, if you want the challenge),
    take this .txt file, and count how many of each "category" of each image there are.
    This text file is actually a list of files corresponding to the SUN database scene recognition database,
    and lists the file directory hierarchy for the images. Once you take a look at the first line or two of the file,
    it will be clear which part represents the scene category. To do this,
    you're going to have to remember a bit about string parsing in Python 3. I talked a little bit about it in this post.

"""
def names_counter():
    with open('name_list.txt') as f:
        lines = f.readlines()

    names = {}

    for name in lines:
        names.setdefault(name, 0)
        names[name] += 1

    return names

# EXTRA
import re
category = {}
# open the file on read mode
with open('image_list.txt') as f:
    # read all the lanes on the file
    lines = f.readlines()
data = []
# strip the line from the '/a/, /b/....'
for line in lines:
    line = re.split(r'[/][a-z][/]+',line)
    line = filter(None, line)
    for i in line:
        data.append(i)

# strip the rest of the line from the 'sun_azwkcepuagjvdjcq.jpg' and put the rest into a list
cat_list = []
for i in data:
    cat = re.findall(r'^[a-z]+[_]*[a-z]*[^/]', i)
    for j in cat:
        cat_list.append(j)
# we put the elements of the list into dictionary
for i in cat_list:
    category.setdefault(i,0)
    category[i] +=1
print category
