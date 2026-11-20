prices = [7, 1, 5, 3, 6, 4]

buy = 0
sell = 0
profit = 0
max_profit = int()

for i in range(len(prices)):
    buy = prices[i]
    for j in range(i+1, len(prices)):
        
        sell = prices[j]
        profit = sell - buy
        if profit > max_profit:
            max_profit = profit

print(max_profit)

#1. mp = 7; 1-7 = -6
#2. mp = 1; 5-1 = 4
#3. mp = 1; 3-1 = 2
#4. mp = 1; 6-1 = 5
#5. mp = 1; 4-1 = 3
#prices = [7, 1, 5, 3, 6, 4]


#base case solution
min = prices[0]
maximum_profit = int()
lst = set()
for i in range(1, len(prices)):
    if prices[i] <= min:
        min = prices[i]

    profit = prices[i] - min
    if profit > maximum_profit:
        maximum_profit = profit

print(maximum_profit)
