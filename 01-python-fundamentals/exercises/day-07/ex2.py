def freq_count(numbers):
    seen = {}
    for i in numbers:
        if i in seen:
            seen[i] += 1
        seen[i] = 1
    return seen



numbers = [2,3,4,3,5,6,7,8,5,6,0]
print(freq_count(numbers))