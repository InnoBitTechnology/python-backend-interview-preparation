numbers = [2, 1, 5, 1, 3, 2]
k = 3

window_sum = sum(numbers[:3])
max_sum = window_sum
for i in range(k, len(numbers)):
    window_sum = window_sum + numbers[i] - numbers[i-k]
    if max_sum < window_sum:
        max_sum = window_sum

print(max_sum)


