# check the prime number or not

def is_prime(n):

    if n <= 1:
        return "Not Prime"

    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return "Not Prime"

    return "Prime"

num = int(input())

print(is_prime(num))
