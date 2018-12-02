from random import sample

a = sample(range(0,100),11)
b = sample(range(0,100), 15)

c = set([i for i in a if i in b])
print c
