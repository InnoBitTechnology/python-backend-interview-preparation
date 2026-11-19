text = input()

if text.lower().replace(" ", "") == text[::-1].lower().replace(" ",""):
    print('palindrome')
else:
    print('not palindrome')
