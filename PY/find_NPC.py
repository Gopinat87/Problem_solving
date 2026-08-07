from collections import Counter

def first_non_repeating(s):
    count = Counter(s)

    for ch in s:
        if count[ch] == 1:
            return ch
    return -1

text = "aabbcdeff"
print(first_non_repeating(text))