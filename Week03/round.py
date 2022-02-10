# This program takes a float and outputs it as an integer (rounded)
# Author: Michael Crampton
# The round function rounds to the nearest even number, so be careful with it's use
numberToRound = float(input("Enter a float number:"))
roundedNumber = round(numberToRound)
print ('{} rounded is {}' .format(numberToRound,roundedNumber))