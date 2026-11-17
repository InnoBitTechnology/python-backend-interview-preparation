numbers = [1, 2, 3, 1]
dup = False
seen = set()
for number in numbers:
    if number in seen:
        dup = True
    else:
        seen.add(number)

if dup:
    print(dup)
else:
    print(dup)

#Time: o(n)
#space: o(n)