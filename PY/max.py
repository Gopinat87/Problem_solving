# Find the Maximum Difference Between Two Elements
# Problem

# Given an array, find the maximum difference arr[j] - arr[i] where j > i.

# You must buy/choose the first element before the second element.

# Input
# [7, 1, 5, 3, 6, 4]
# Output
# 5

# Because:

# 6 - 1 = 5
# 🐍 Python

def max_difference(arr):

    min_value = arr[0]
    max_difference = arr[1] - arr[0]

    for i in range(1, len(arr)):

        difference = arr[i] - min_value

        if difference > max_difference:
            max_difference = difference

        if arr[i] < min_value:
            min_value = arr[i]

    return max_difference


arr = [7, 1, 5, 3, 6, 4]

print(max_difference(arr))