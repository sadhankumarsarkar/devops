#Write a program that checks whether a given number is prime using a for loop and if condition

# # Function to check if a number is prime
def is_prime(number):
    if number <= 1:
        return False  # Numbers less than or equal to 1 are not prime

    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False  # Found a divisor, number is not prime

    return True  # No divisors found, number is prime

# Input: Number to check
num = int(input("Enter a number: "))

# Check and display the result
if is_prime(num):
    print(f"{num} is a prime number.")
else:
    print(f"{num} is not a prime number.")