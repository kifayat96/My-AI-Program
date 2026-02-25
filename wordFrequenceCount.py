def word_frequency(sentence):
    words = sentence.split()
    freq = {}
    for w in words:
        freq[w] = freq.get(w, 0) + 1
    return freq

print(word_frequency("AI is AI and AI is powerful"))
