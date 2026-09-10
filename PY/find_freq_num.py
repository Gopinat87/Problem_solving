# Find the Most Frequent Element
# Question

# Given an array, find the element that appears most frequently.

# If two elements have the same frequency, return the one that appears first in the array.

# Example
# Input:
# [4, 2, 4, 3, 2, 4, 2]

# Output:
# 4

# 4 appears 3 times, while 2 appears 3 times too — but 4 appears first.

def most_frequent(arr):

    frequency = {}

    for num in arr:
        frequency[num] = frequency.get(num, 0) + 1

    max_count = 0
    answer = arr[0]

    for num in arr:

        if frequency[num] > max_count:
            max_count = frequency[num]
            answer = num

    return answer


arr = [4, 2, 4, 3, 2, 4, 2]

print(most_frequent(arr))