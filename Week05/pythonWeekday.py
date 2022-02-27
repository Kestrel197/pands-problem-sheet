# This programm tell you if it's the weekend or not.
# Part of solution found at: https://www.w3schools.com/python/python_datetime.asp
import datetime
x = datetime.datetime.now()
y = (x.strftime("%A"))
if (y == "Saturday" or "Sunday"):
    print ("It is the weekend, yay!")
elif y != ("Saturday" or "Sunday"):
    print ("Yes, unfortunately today is a weekday.")