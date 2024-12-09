# Given list
numbers = [10, 501, 22, 37, 100, 999, 87, 351]

# Lists to store even and odd numbers
even_numbers = []
odd_numbers = []

# Loop through the list to classify even and odd numbers
for num in numbers:
    if num % 2 == 0:
        even_numbers.append(num)
    else:
        odd_numbers.append(num)

# Output the even and odd lists
print("Even numbers:", even_numbers)
print("Odd numbers:", odd_numbers)