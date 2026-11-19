text1 = input()
text2 = input()

text1freq = {}
text2freq = {}

for ch in text1:
    if ch in text1freq:
        text1freq[ch] += 1
    else:
        text1freq[ch] = 1

for ch in text2:
    if ch in text2freq:
        text2freq[ch] += 1
    else:
        text2freq[ch] = 1

print(text1freq == text2freq)

