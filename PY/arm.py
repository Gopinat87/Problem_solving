# Check Armstrong Number
# Question

# A number is an Armstrong number if the sum of each digit raised to the power of the number of digits equals the original number.

# Example:

# 153

# Because:

# 1³ + 5³ + 3³ = 153
# Output
# Armstrong Number

def is_armstrong(n):
    original = n
    digits = len(str(n))
    total = 0

    while n > 0:
        digit = n % 10
        total += digit ** digits
        n //= 10

    return total == original


num = 153

if is_armstrong(num):
    print("Armstrong Number")
else:
    print("Not Armstrong Number")