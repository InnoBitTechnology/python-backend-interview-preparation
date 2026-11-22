x = 50
z = 1000
def all_func(x,z):
    print(f'x is: {x}')
    x += 50
    print(f'x after adding 50: {x}')
    y = 10
    print(f'y created locally: {y}')
    z=500
    print(f'z is: {z}')


all_func(x,z)
#local func: error y is not definded - Because it's a local variable
#print(y)
print(x)
print(f'priting z outside the function: {z}')
    