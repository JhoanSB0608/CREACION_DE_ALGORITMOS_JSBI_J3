def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def is_palindrome_binary(num):
    binary_representation = bin(num)[2:]
    return binary_representation == binary_representation[::-1]

def main():
    n = 10

    palindrome_primes = []
    count = 0
    num = 2

    while count < n:
        if is_prime(num) and is_palindrome_binary(num):
            palindrome_primes.append(num)
            count += 1
        num += 1

    print(f"Los primeros {n} números primos cuya representación binaria es un palíndromo son:")
    print(palindrome_primes)

if __name__ == "__main__":
    main()


def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True

def nth_prime(n):
    count = 0
    num = 2
    while count < n:
        if is_prime(num):
            count += 1
        num += 1
    return num - 1

def product_of_digits(num):
    product = 1
    for digit in str(num):
        product *= int(digit)
    return product

def main():
    n = 100

    for i in range(1, n + 1):
        prime = nth_prime(i)
        product_digits = product_of_digits(prime)

        if product_digits == i:
            print(f"Para el {i}-ésimo primo ({prime}), el producto de sus dígitos ({product_digits}) es igual a {i}.")

if __name__ == "__main__":
    main()