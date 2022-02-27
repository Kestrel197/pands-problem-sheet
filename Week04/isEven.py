# This program informs the user if the integer they have entered is even or odd
# Author: Michael Crampton
number = int(input("enter an integer:"))
if (number % 2) == 0:
    print ("{} is an even number".format(number))
else:
    print("{} is an odd number".format(number))