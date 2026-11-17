lst = [10, 4, 25, 7, 5]
largest = 0
tbs = lst[0]
for i in range(1, len(lst)):
    if tbs < lst[i]:
        tbs = lst[i]
print(tbs)