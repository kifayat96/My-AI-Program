def word_count(s):
    count = 0
    word = ""
    for ch in s:
        if ch != " ":
            word += ch
        else:
            if word != "":
                count += 1
                word = ""
    if word != "":
        count += 1
    return count

print(word_count("AI is very powerful"))
