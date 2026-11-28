def long_substring(s):
    unique_set = set()
    left = 0
    max_lenth = 0
    for right in range(len(s)):
        while s[right] in unique_set:
            unique_set.remove(s[left])
            left += 1
        unique_set.add(s[right])
        max_lenth = max(max_lenth, right-left + 1)
    print(right,left)
    return max_lenth

def substring_dict(s):

    dict_index = {}
    left = 0
    max_length = 0

    for i in range(len(s)):
        if s[i] in dict_index and dict_index[s[i]] >= left:
            left = dict_index[s[i]] + 1
        dict_index[s[i]] = i
        max_length = max(max_length, i-left +1)
    return max_length


s = "abcbcde"
#.   0123456
print(substring_dict(s))