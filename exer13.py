"""
Write a program that asks the user how many Fibonnaci numbers to generate and then generates them.
Take this opportunity to think about how you can use functions.
Make sure to ask the user to enter the number of numbers in the sequence to generate
"""
def fibonnaci_numbers():
    a = int(raw_input('Please input number: '))
    if a==1:
        b=[1]
    elif a!=1:
        b=[1,1]
        for i in b:
            if len(b)<a:
                i=b[-1]+b[-2]
                b.append(i)
    print b

if __name__ == '__main__':
    fibonnaci_numbers()
