# Find the missing number from the range 1 to n.
# Assumption: exactly one number is missing and there are no duplicates.

numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]
n = 10

expected_sum = n * (n + 1) // 2
actual_sum = 0

for num in numbers:
    actual_sum += num

missing = expected_sum - actual_sum

print("Missing number:", missing)
