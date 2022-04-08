# A program to convert amounts in dollars to cents, will work even on minus dollar amounts.
# Author: Michael Crampton
amount = float(input("Please enter an amount:$")) 
# For code line 7, to remove the decimal point the amount must be converted to an integer,
# we need an absolute value to remove any possible minus figures entered and
# then multiply by 100 to get the value in cents from dollars.
absoluteValue = int(abs(amount*100))
print ('That amount in cent is :'+ str(absoluteValue)) # Must convert (absoluteValue) to string in order to concate correctly