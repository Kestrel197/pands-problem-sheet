# This program informs rounds the user entered number and outputs whether it's odd or even
# There's arguements as what the correct way to round is so I stuck with Pythons'
# "bankers rounding" out of simplicity.
# Author: Michael Crampton
number = float(input("enter the percentage:"))
roundedNumber = round(number)
if (roundedNumber % 2) == 0:
    print ("{} is an even number".format(roundedNumber))
else:
    print("{} is an odd number".format(roundedNumber))