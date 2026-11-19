def reverse_list(numbers):
    reversed = []
    for i in numbers:
        reversed.insert(0, i)
    return reversed


numbers = [10, 20, 30, 40, 50]
print(reverse_list(numbers))
print(numbers[::-1])