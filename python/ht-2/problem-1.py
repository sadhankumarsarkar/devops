#Write a program that calculates the sum of numbers from 1 to N and checks if the sum is even or odd using a for loop and if condition

# Input: N (positive integer)
N = int(input("Enter a Number (N): "))

# Initialize sum
total_sum = 0

# Calculate the sum using a for loop
for i in range(1, N + 1):
    total_sum += i

# Check if the sum is even or odd
if total_sum % 2 == 0:
    print(f"The sum of numbers from 1 to {N} is {total_sum}, which is even.")
else:
    print(f"The sum of numbers from 1 to {N} is {total_sum}, which is odd.")