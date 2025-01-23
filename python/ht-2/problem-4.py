#Write a program that counts down from N to 1 using a while loop and checks if the number is even or odd at each step

# Input: N (positive integer)
N = int(input("Enter a Number (N): "))

# Validate input
if N <= 0:
    print("Please enter a Number.")
else:
    # Countdown using a while loop
    while N >= 1:
        if N % 2 == 0:
            print(f"{N} is even.")
        else:
            print(f"{N} is odd.")
        N -= 1  # Decrement the number