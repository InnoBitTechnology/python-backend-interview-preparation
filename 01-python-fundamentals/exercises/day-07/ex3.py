def unique_value(numbers):
    seen = {}
    for i in numbers:
        if i in seen:
            continue
        else:
            seen[i] = 1
    return list(seen.keys())



numbers = [1,2,3,4,5,6,7,4,5,8,9,0]
print(unique_value(numbers))