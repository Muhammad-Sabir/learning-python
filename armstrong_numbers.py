# Write a Python program to find all Armstrong numbers within a specified range.

def is_armstrong_number(num):
    sum = 0
    temp = num

    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    
    return sum == num

lower_limit = int(input("Enter the lower limit: "))
upper_limit = int(input("Enter the upper limit: "))

armstrong_numbers = list(filter(is_armstrong_number, range(lower_limit, upper_limit + 1)))

print(f"Armstrong numbers between {lower_limit} and {upper_limit} are: {armstrong_numbers}")