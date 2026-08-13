# Find the Intersection of Two Arrays
# Question

# Given two arrays, find the elements that appear in both arrays, including duplicates based on their frequency.

# Input

# arr1 = [1, 2, 2, 3, 4]
# arr2 = [2, 2, 4, 5]

# Output

# [2, 2, 4]

def intersection(arr1, arr2):

    frequency = {}

    for num in arr1:
        frequency[num] = frequency.get(num, 0) + 1

    result = []

    for num in arr2:
        if frequency.get(num, 0) > 0:
            result.append(num)
            frequency[num] -= 1

    return result


arr1 = [1, 2, 2, 3, 4]
arr2 = [2, 2, 4, 5]

print(intersection(arr1, arr2))