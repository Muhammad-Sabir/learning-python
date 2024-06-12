# Write a Python program to find the factorial of a number input by the user.

def get_factorial(num):
    if num == 0 or num == 1:
        return 1
    if num == 2:
        return 2
    
    return num * get_factorial(num - 1)

num = int(input("Enter a number: "))

print(get_factorial(num))