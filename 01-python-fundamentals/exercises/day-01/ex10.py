a,b,c = 10,50,25

print(max(a,b,c))
print(min(a,b,c))
print((a+b+c)/3)

if a > b and a>c:
    print(f"max: {a}")
elif b>a and b>c:
    print(f"max: {b}")
else:
    print(f"Max: {c}")

if a < b and a<c:
    print(f"min: {a}")
elif b<a and b<c:
    print(f"min: {b}")
else:
    print(f"Min: {c}")