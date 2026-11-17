def grade(num):
    if num >= 90 and num <= 100:
        print('A')
    elif num >= 75 and num < 90:
        print('B')
    elif num >= 60 and num < 75:
        print('C')
    elif num >= 40 and num < 60:
        print('D')
    elif num < 40 and num >= 0:
        print('F')
    elif num > 100:
        print(f"Number is greater than 100: {num}")
    else:
        print(f"Number is negative: {num}")

def main():
    num = int(input("Enter a number: "))

    grade(num)

if __name__ == "__main__":
    main()