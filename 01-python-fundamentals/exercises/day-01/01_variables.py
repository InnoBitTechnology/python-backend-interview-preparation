def main():
    name = 'Mohit'
    age = 22
    salary = 100000
    city = 'Noida'
    is_employed = True
    print(name, type(name))
    print(age, type(age))
    print(salary, type(salary))
    print(city, type(city))
    print(is_employed, type(is_employed))

def exercise1():
    print("exercise 1".center(40, "="))
    a = 20
    b = 6
    print("sum is: ", (a+b))
    print("diff is: ", (a-b))
    print("mul is: ", (a*b))
    print("divison is: ", (a/b))
    print("floor is: ", (a//b))
    print("exponential is: ", (a**b))
    print("remainder is: ", (a%b))

def exercise2(first_name,last_name):
    print("exercise 2".center(40, "="))
    print(first_name+" "+last_name)

def exercise3(age):
    if age > 18:
        print("Adult")
    else:
        print("Minor")

'''
Exercide 5, 6 & 7: predict the output before executing:
5:
x = 10
y = "10"

print(type(x))
print(type(y))
print(x == y)

6:
a = 10
b = 3

print(a / b)
print(a // b)
print(a % b)

7:
x = "100"

print(type(x))

x = int(x)

print(type(x))
print(x + 50)'''

'''
Exercise 8 — Interview-style
Explain why this fails:
age = 25
name = "Manoj"
print(age + name)


Then fix it.'''

def exercise8():
    age = 25
    name = "Manoj"
    print(str(age)+name)

def exe9():
    a = 100
    b = 200
    a,b = b,a
    print(a, b)

'''
Exercise 10 — Important
Predict:
print(bool(0))
print(bool(1))
print(bool(""))
print(bool("Python"))
print(bool(None))'''

if __name__ == "__main__":
    main()
    exercise1()
    exercise2("mohit", "Sharma")
    print("exercise 3".center(40, "="))
    exercise3(28)
    print("exercise 8".center(40, "="))
    exercise8()
    print("exercise 9".center(40, "="))
    exe9()
