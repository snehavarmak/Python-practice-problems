def count_vowels(s):
    count = 0
    for char in s.lower():
        if char in "aeiou":
           count += 1
    return count
print(count_vowels("education"))
