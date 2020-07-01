#simple program to add all the numbers in the specified range

# create a variable
def multiples_of_3_or_5():

#range of the program
    for number in range(1000):

#number % 3 and number % 5 represent numbers in the given range 
#divisble by 3 & 5        
        if not number % 3 or not number % 5:
            yield number

#you may find variants of this code that don't have parathesis in the them
#that seems to be related to python 2, as the syntax in python 3 requires it
print(sum(multiples_of_3_or_5()))