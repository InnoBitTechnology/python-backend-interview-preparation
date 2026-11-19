#two sum - normal
'''
def two_sum(number, target):
    for i in range(len(number)+1):
        diff = target - number[i]
        if diff in number:
            return i,number.index(diff)
'''

#optimized
def two_sum(numbers, target):
    seen = {}

    for i, number in enumerate(numbers):
        diff = target - number

        if diff in seen:
            return [seen[diff], i]

        seen[number] = i

    return []

numbers = [2, 7, 11, 5, 15] 
target = 7
print(two_sum(numbers, target))
