# This program asks the user to input a filename in the command line and then
# counts the number of e's in that file.
import sys
filename = sys.argv[0]
sys.argv[0] = input("Please enter a filename:")
with open(sys.argv[0]) as f:
        data = f.read()
        x = data.count("e")

print("The number of e's in this file is:",str(x))