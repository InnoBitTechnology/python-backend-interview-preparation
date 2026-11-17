num = int(input())
newnum = 0
rem = 0
while num > 0:
    rem = num % 10
    newnum = newnum*10 + rem
    num //= 10
print(newnum)