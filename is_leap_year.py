# Write a Python program to check if a given year is a leap year.

import calendar

year = int(input("Enter the year: "))

print(f"{year} is a leap year.") if calendar.isleap(year) else print(f"{year} is not a leap year.")