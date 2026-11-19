text = "programming"
newtxt = ""
for ch in text:
    if ch in newtxt:
        continue
    else:
        newtxt += ch

print(newtxt)