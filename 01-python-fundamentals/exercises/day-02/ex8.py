#primnumber:
num = int(input())
prime = True
for i in range (2, num//2):
    if num % i == 0:
        prime = False
if prime:
    print("Prime")
else:
    print('not prime')
