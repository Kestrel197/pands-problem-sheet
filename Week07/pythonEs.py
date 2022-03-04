import sys
filename = input("Please enter a filename:")
with open(sys.argv[filename], 'r') as f:
    data = f.read()
    x = data.count("e")

print("The number of e's in this file is:",str(x))