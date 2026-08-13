# Find the Longest Word with Unique Characters
# Question

# Given a sentence, find the longest word that contains no repeated characters.

# Input

# "apple dog house banana"

# Output

# house

# Because:

# apple   → p repeats
# dog     → unique
# house   → unique
# banana  → a repeats

def longest_unique_word(sentence):

    words = sentence.split()
    longest = ""

    for word in words:

        if len(set(word)) == len(word):

            if len(word) > len(longest):
                longest = word

    return longest


sentence = "apple dog house banana"

print(longest_unique_word(sentence))