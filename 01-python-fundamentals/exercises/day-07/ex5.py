def check_prime(number):
    prime = True
    prime_numbers = []
    for i in range (2, number):
        if number % i == 0:
            prime = False
        else:
            prime_numbers.append(i)

    return prime, prime_numbers


number = int(input())
print(check_prime(number))