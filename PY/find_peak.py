# Find the Peak Element
# Question

# An element is called a peak element if it is greater than its immediate neighbors.

# Find any peak element.

# For the first and last elements, consider only their single neighbor.

# Example
# Input:
# [1, 3, 20, 4, 1, 0]

# Output:
# 20

# Because:

# 3 < 20 > 4

# So 20 is a peak.

def find_peak(arr):

    n = len(arr)

    if n == 1:
        return arr[0]

    if arr[0] > arr[1]:
        return arr[0]

    if arr[n - 1] > arr[n - 2]:
        return arr[n - 1]

    for i in range(1, n - 1):

        if arr[i] > arr[i - 1] and arr[i] > arr[i + 1]:
            return arr[i]

    return -1


arr = [1, 3, 20, 4, 1, 0]

print(find_peak(arr))