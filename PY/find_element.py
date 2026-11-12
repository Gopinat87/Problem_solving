a = [10, 20, 30, 40, 50]
b = [30, 40, 50, 60, 70]

common = []

for num in a:

    if num in b and num not in common:
        common.append(num)

print("Common elements:", common)