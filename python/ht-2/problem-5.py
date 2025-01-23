#Write a program that takes a list of numbers and returns the sum of positive numbers, the count of negative numbers, and the largest number in the list

def analyze_numbers(numbers):
    # Initialize variables
    positive_sum = 0
    negative_count = 0
    largest_number = numbers[0] if numbers else None  # Handle empty list case

    for num in numbers:
        if num > 0:
            positive_sum += num
        elif num < 0:
            negative_count += 1
        
        # Update largest_number
        if largest_number is None or num > largest_number:
            largest_number = num

    return positive_sum, negative_count, largest_number

# Input: List of numbers
numbers = list(map(float, input("Enter a list of numbers separated by spaces: ").split()))

# Analyze the list
positive_sum, negative_count, largest_number = analyze_numbers(numbers)

# Output results
print(f"Sum of positive numbers: {positive_sum}")
print(f"Count of negative numbers: {negative_count}")
if largest_number is not None:
    print(f"Largest number in the list: {largest_number}")
else:
    print("The list is empty.")