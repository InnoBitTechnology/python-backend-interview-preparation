def checknum(num):
    if num > 0:
        print('Positive')
    elif num == 0:
        print('Zero')
    else:
        print('Negative')

def main():
    num = int(input("Enter a number: "))

    checknum(num)

if __name__ == "__main__":
    main()