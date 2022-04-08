# This program reads in a string and strips any leading or trailing spaces.
# It also converts all the letters to lower case and outputs the length 
# of the original string and the normalised one.
rawString = input("please enter a string:")
normalisedString = rawString.strip().lower()
lenghtOfRawString = len(rawString)
lenghtOfNormalised = len(normalisedString)
print("That String normalised is :{}".format(normalisedString))
print("We reduced the input string from {} to {} characters".format(
lenghtOfRawString, lenghtOfNormalised ))