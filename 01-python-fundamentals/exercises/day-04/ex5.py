def is_palindrome(text):
    if text == text[::-1]:
        return True
    return False

text = input()
print(is_palindrome(text))