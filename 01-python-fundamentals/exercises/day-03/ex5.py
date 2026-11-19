def occer(numbers, check_num):
    count = 0
    for i in numbers:
        if i == check_num:
            count += 1
    return count
    

numbers = [1, 2, 3, 2, 4, 2, 5]
check_num = int(input('Enter number to check the occurance of: '))
print(occer(numbers, check_num))
