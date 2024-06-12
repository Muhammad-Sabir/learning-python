# Write a Python program that performs addition, subtraction, multiplication, and division of two numbers input by the user.

def add (a, b):
    return a + b

def subtract (a, b):
    return a - b

def multiply (a, b):
    return a * b

def divide (a, b):
    return a / b


num_one = int(input("Enter first number: "))
num_two = int(input("Enter second number: "))

print(f"{num_one} + {num_two} = {add(num_one, num_two)}")
print(f"{num_one} - {num_two} = {subtract(num_one, num_two)}")
print(f"{num_one} * {num_two} = {multiply(num_one, num_two)}")
print(f"{num_one} / {num_two} = {divide(num_one, num_two)}")
