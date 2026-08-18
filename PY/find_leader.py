# Find the Leaders in an Array
# Question

# An element is called a leader if it is greater than all elements to its right.

# Find all leaders in the array.

# Input
# [16, 17, 4, 3, 5, 2]
# Output
# [17, 5, 2]

def find_leaders(arr):

    leaders = []
    max_right = float('-inf')

    for i in range(len(arr) - 1, -1, -1):

        if arr[i] > max_right:
            leaders.append(arr[i])
            max_right = arr[i]

    leaders.reverse()

    return leaders


arr = [16, 17, 4, 3, 5, 2]

print(find_leaders(arr))