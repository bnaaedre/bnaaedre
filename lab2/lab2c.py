#!/usr/bin/env python3

# Importing the sys module
import sys

# Assigning the first command line argument to the name variable
name = sys.argv[1]

# Assigning the second command line argument to the age variable
age = int(sys.argv[2])

# Print the greeting message with the user's name and age
print("Hi {}, you are {} years old.".format(name, age))

