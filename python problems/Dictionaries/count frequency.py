elements = [1, 2, 2, 3, 3, 3]
frequency = {}

for item in elements:
    if item in frequency:
        frequency[item] += 1
    else:
        frequency[item] = 1

print("Frequency:", frequency)
