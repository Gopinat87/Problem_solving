# Find the Second Most Frequent Character
# Question

# Given a string, find the character with the second highest frequency.

# Example
# Input:
# "banana"

# Output:
# "a"

# Frequency:

# a → 3
# n → 2
# b → 1

# So a is the most frequent, and n is the second most frequent.

# Therefore, actually:

# Output:
# n

def second_most_frequent(s):

    frequency = {}

    for ch in s:
        frequency[ch] = frequency.get(ch, 0) + 1

    counts = sorted(set(frequency.values()), reverse=True)

    if len(counts) < 2:
        return -1

    second_count = counts[1]

    for ch in s:
        if frequency[ch] == second_count:
            return ch

    return -1


s = "banana"

print(second_most_frequent(s))