# Write a Python program to print all prime numbers within a specified range.

def is_prime(num):
    if num <= 1:
        return False
    if num <= 3: 
        return True
    
    for i in range(2, int(num**0.5) + 1): # previously used (num // 2) - which isn't the most efficient way
        if num % i == 0:
            return False
        
    return True
    
lower_limit = int(input("Enter lower limit for prime numbers: "))
upper_limit = int(input("Enter upper limit for prime numbers: "))

prime_numbers = list(filter(is_prime, range(lower_limit, upper_limit + 1)))

print(prime_numbers)