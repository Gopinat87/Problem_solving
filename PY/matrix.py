# find the Sum of Both Diagonals in a Matrix
# Question

# Given a square matrix, find the sum of both diagonals.

# Input
# 1 2 3
# 4 5 6
# 7 8 9
# Output
# 25

# Explanation:

# Primary diagonal:   1 + 5 + 9 = 15
# Secondary diagonal: 3 + 5 + 7 = 15

# Since 5 is common to both diagonals:

# 15 + 15 - 5 = 25

def diagonal_sum(matrix):

    n = len(matrix)
    total = 0

    for i in range(n):

        total += matrix[i][i]

        if i != n - 1 - i:
            total += matrix[i][n - 1 - i]

    return total


matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(diagonal_sum(matrix))