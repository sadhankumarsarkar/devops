#Write a program to generate the Fibonacci sequence up to N terms using a while loop and a function

# Function to generate Fibonacci sequence
def generate_fibonacci(n):
    # List to store Fibonacci sequence
    fibonacci_sequence = []
    # Initialize first two terms
    a, b = 0, 1
    count = 0

    # Generate the N sequence using a while loop
    while count < n:
        fibonacci_sequence.append(a)
        a, b = b, a + b
        count += 1

    return fibonacci_sequence

# Input: Number of terms (N)
N = int(input("Enter the number of terms (N): "))

# Ensure N is positive
if N <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and print the Fibonacci sequence
    fibonacci_sequence = generate_fibonacci(N)
    print(f"The Fibonacci sequence with {N} terms is: {fibonacci_sequence}")