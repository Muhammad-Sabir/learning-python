# Write a Python program to calculate and print the sum of the first ten natural numbers.

# Using loop

sum = 0

for i in range(1, 11):
    sum += i

print(f"Sum of first ten natural numbers using loop: {sum}")

# Using summation formulae

n = 10

sum = n * (n + 1) // 2

print(f"Sum of first ten natural numbers using formulae: {sum}")