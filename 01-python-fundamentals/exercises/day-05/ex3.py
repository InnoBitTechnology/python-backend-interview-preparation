def calculate_sum(*args):
    sum = 0
    for i in args:
        sum += i
    return sum


print(calculate_sum(5,10,50))
print(calculate_sum(5,10,50,100))