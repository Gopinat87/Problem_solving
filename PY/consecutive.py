# Compress Consecutive Characters
# Question

# Given a string, replace consecutive repeated characters with the character followed by its count.

# Input
# aaabbccccd
# Output
# a3b2c4d1

# Another example:

# Input:
# aabbc


# Output:
# a2b2c1

def compress_string(s):

    if not s:
        return ""

    result = ""
    count = 1

    for i in range(1, len(s)):

        if s[i] == s[i - 1]:
            count += 1

        else:
            result += s[i - 1] + str(count)
            count = 1

    result += s[-1] + str(count)

    return result


s = "aaabbccccd"

print(compress_string(s))