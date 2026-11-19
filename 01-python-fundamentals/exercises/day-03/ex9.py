def frequency_counter(numbers):
    seen = {}
    for i in numbers:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    return seen

numbers = [1, 2, 2, 3, 1, 4, 2, 3, 3]
print(frequency_counter(numbers))