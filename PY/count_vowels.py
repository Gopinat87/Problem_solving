def count_vowels(text):
    count = 0

    for ch in text.lower():
        if ch in "aeiou":
            count += 1

    return count

word = input("Enter a string: ")
print(count_vowels(word))