def linear_search(numbers, target):
    for i in range(len(numbers)):
        if target == numbers[i]:
            return i
    else:
        return -1


numbers = [10, 25, 7, 42, 19, 31] 
target = 42

print(linear_search(numbers, target))

#1. What is the best-case time complexity?: o(1)
#2. What is the worst-case time complexity?: o(n)
#3. What is the space complexity?: o(1)
#4. Why can't we simply use binary search on any list? Because the list usually are not sorted and binary search works best with the sorted elements.
