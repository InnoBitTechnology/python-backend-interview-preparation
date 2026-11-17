#primnumber:
num = int(input())
prime = True
n = num//2
for i in range (2, n+1):
    if num % i == 0:
        prime = False
if prime:
    print("Prime")
else:
    print('not prime')
