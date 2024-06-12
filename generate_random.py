# Write a Python program to generate and print a random number between a specified range.

import random

print("*-----GENERATING RANDOM NUMBER IN RANGE-----*", end="\n \n")
lower_limit = int(input("Enter the lower limit of range: "))
upper_limit = int(input("Enter the upper limit of range: "))

random_int = random.randint(lower_limit, upper_limit)

print(random_int)
