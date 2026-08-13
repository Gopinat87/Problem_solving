#Find the Sum of Digits


def sum_of_digits(n):
    total = 0

    while n > 0:
        digit = n % 10
        total += digit
        n //= 10

    return total


num = 12345
print(sum_of_digits(num))