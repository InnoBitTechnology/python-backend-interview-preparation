def freq(text):
    frequency = {}
    for ch in text:
        if ch in frequency:
            frequency[ch] += 1
        else:
            frequency[ch] = 1
    return frequency


text = "Python Backend Developer"
print(freq(text))