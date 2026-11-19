def find_smallest(numbers):
    smallest = numbers[0]
    for i in range(1, len(numbers)):
        if numbers[i] < smallest:
            smallest = numbers[i]
    return smallest


numbers = [10, 25, 7, 42, 19, 31, -1]
print(find_smallest(numbers))