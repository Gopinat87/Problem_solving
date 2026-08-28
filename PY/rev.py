# Reverse Words in a Sentence
# Problem

# Reverse the order of words, but don't reverse the characters inside each word.

# Input

# "I love Python"

# Output

# "Python love I"

def reverse_words(sentence):
    words = sentence.split()
    words.reverse()
    return " ".join(words)


sentence = "I love Python"

print(reverse_words(sentence))