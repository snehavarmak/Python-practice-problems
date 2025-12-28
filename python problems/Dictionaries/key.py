scores = {
    "Alice": 85,
    "Bob": 92,
    "Charlie": 88
}

max_key = max(scores, key=scores.get)
print("Key with maximum value:", max_key)
