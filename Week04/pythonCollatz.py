# This program prompts the user to enter a positive integer
# and then runs a collatz sequence. The program stops once the
# sequence hits 1.
# I found this to be very difficult code to write and after multiple attempts
# I found a solution at: https://www.youtube.com/watch?v=lAp_5qTdOhM
def collatz(n):
    if (n % 2 == 0):
        return n // 2
    elif (n % 2 == 1):
        return ((n * 3) + 1)
n = int(input("Enter any positive integer:"))
while (n != 1):
    n = collatz(n)
    print (n)