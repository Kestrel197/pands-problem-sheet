#A prgram that asks a user to input a string and outputs every second letter in reverse order.
# Author: Michael Crampton
string = input('Please enter a sentence:')
# The slice function used below was found on w3schools and stackoverflow, 
# still not quite sure how the notation works for it, but this seems good.
print (string[::-2])