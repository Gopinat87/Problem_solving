# Find the Smallest Missing Positive Number
# Problem

# Given an unsorted array, find the smallest positive integer that is missing.

# Input

# [3, 4, -1, 1]

# Output

# 2

# Because 1 exists, but 2 is missing.

# More examples
# [1, 2, 0] → 3
# [7, 8, 9, 11] → 1
# 🐍 Python

def smallest_missing_positive(arr):

    positive = set()

    for num in arr:
        if num > 0:
            positive.add(num)

    number = 1

    while number in positive:
        number += 1

    return number


arr = [3, 4, -1, 1]

print(smallest_missing_positive(arr))