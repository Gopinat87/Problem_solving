numbers = [1, 2, 3, 4, 6, 7, 8, 9, 10]

n = 10

total = n * (n + 1) // 2

actual_sum = sum(numbers)

missing = total - actual_sum

print("Missing number:", missing)