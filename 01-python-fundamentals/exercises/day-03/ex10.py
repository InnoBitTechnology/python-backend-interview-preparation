def first_unique(numbers):
    seen = {}
    for i in numbers:
        if i in seen:
            seen[i] += 1
        else:
            seen[i] = 1
    for key,value in seen.items():
        if value == 1:
            print(key)
            break

numbers = [4, 5, 1, 2, 1, 5, 4, 3]
first_unique(numbers)