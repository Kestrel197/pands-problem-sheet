from logging import exception
# I had great difficulty actually understanding Newton's method so found a 
# solution in terms of writing the code (that I think meets weekly task criteria 
# while simply asking the user to input a positive number) here: 
# https://hackernoon.com/calculating-the-square-root-of-a-number-using-the-newton-raphson-method-a-how-to-guide-yr4e32zo
# The program will request the user try again if they enter letters
# but I haven't found a way to do that if the enter a negative number.
def sqrt(n):
    r = n
    precision = 10 ** (-10)
    while abs(n - r * r) > precision:
        r = (r + n / r) / 2
    return r

n = True

while (n == True):
    try:
        n = int(input("Please enter a positive number:"))
    except ValueError:
        print ("Please try again")
n1 = round((sqrt(n)),3)
print ("The square root of",str(n),"is approx.",str(n1))