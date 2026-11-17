principal = int(input())
rate=int(input())
time=int(input())

si = (principal*rate*time)/100
am = principal + si

print(f"Simple Interest: ", si)
print(f"Amount: ", am)