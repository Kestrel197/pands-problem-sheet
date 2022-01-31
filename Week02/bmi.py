# This is a prgram that calculates a persons' BMI
# Author: Michael Crampton
weightcm = int(65)
heightkg = int(180)
bmi = ((weightcm / heightkg) / heightkg) * 10000 
print (round (bmi, 2)) # Found command on "How to round decimal digits up and down in Python?" on Kodify.net