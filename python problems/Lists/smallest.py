numbers = [10, 45, 23, 89, 5]
smallest = numbers[0]

for num in numbers:
    if num < smallest:
        smallest = num

print("Smallest element:", smallest)
