numbers = [0, 1, 0, 3, 12, 0, 5]

result = []

for num in numbers:

    if num != 0:
        result.append(num)

zero_count = numbers.count(0)

result.extend([0] * zero_count)

print(result)