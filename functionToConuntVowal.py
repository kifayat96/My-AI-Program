def count_vowels(s):
    count = 0
    for c in s:
        if c in "aeiou":
            count += 1
    return count

print(count_vowels("hello"))
