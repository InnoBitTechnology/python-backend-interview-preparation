text = "aabbcdde"
freq = {}
for ch in text:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

for key,value in freq.items():
    if value == 1:
        print(key)
        break
        