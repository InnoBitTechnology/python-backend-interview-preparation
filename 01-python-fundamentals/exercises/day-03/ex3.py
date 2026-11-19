def find_larget(numbers):
    largest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] > largest:
            largest = numbers[i]
    return largest


numbers = [10, 25, 7, 42, 19, 31]
print(find_larget(numbers))