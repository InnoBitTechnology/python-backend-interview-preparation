def check_anagram(text1, text2):
    dict1 = {}
    dict2 = {}
    anagram = False
    for i in text1:
        if i in dict1:
            dict1[i] += 1
        else:
            dict1[i] = 1
    for i in text2:
        if i in dict2:
            dict2[i] += 1
        else:
            dict2[i] = 1

    if dict1 == dict2:
        anagram = True

    return anagram 


print(check_anagram(text1='silent', text2='listen'))
print(check_anagram("hello", "world"))