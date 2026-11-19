def reverse_string(text):
    newtxt = ""
    for ch in text:
        newtxt = ch + newtxt
    return newtxt


text = str(input())
print(reverse_string(text))