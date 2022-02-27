# This programm keeps asking for an integer from the user until they
# enter an integer less than 0. It also prompts the user to enter smaller numbers
# to speed up the process.
# Author: Michael Crampton
number = int(input("enter an integer:"))
while number >= 0:
    print ("Less than that")
    number = int(input("enter an integer:"))
if number < 0:
    print ("Well done")