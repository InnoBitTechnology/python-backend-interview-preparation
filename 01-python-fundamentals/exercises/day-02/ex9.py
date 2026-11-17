def is_palindrome(text):
    newword = ""
    for ch in text:
        newword = ch + newword
    if text == newword:
        return True
    else:
        return False


text = str(input())
print(is_palindrome(text))