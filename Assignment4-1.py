"""
This program calculates prices for custom house signs.
"""

# Declare and initialize variables here.
charge = float(0.00)
numChars = (18)
color = "black"
woodType = "oak"


if (numChars > 5):
    charge = 35.00 + (numChars-5) * 4
elif numChars > 0:
    charge = 35.00
    
if woodType == "oak":
    charge += 20 
 
if color == "gold":
    charge += 15

# Output Charge for this sign.
print("The charge for this sign is $" + str(charge))