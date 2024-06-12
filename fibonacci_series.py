# Write a Python program to print the Fibonacci sequence up to a specified number of terms.

def get_fibonacci(num):
    if num == 0: return 0
    if num == 1: return 1

    return get_fibonacci(num - 1) + get_fibonacci(num - 2)

limit = int(input("Enter a number upto which you want to print fibonacci sequences: "))

fibonacci_sequence = list(map(get_fibonacci, range(limit + 1)))

print(fibonacci_sequence)