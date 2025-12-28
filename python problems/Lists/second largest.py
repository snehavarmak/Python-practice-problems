numbers = [10, 20, 45, 8, 30]

numbers = list(set(numbers))  # remove duplicates
numbers.sort()

print("Second largest element:", numbers[-2])
