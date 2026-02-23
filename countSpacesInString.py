def count_spaces(s):
    count = 0
    for ch in s:
        if ch == " ":
            count += 1
    return count

print(count_spaces("Artificial Intelligence"))