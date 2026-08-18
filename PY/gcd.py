# Find the GCD of Two Numbers
# Question

# Find the Greatest Common Divisor (GCD) of two numbers.

# Input
# 48, 18
# Output
# 6

def gcd(a, b):
    while b != 0:
        a, b = b, a % b

    return a


print(gcd(48, 18))