def reverse_string(text):
    return text[::-1]

word = input("Enter a string: ")
print(reverse_string(word))

#without slicing

def reverse_string(text):
    reverse = ""
    for ch in text:
        reverse = ch + reverse
    return reverse

word = input("Enter a string: ")
print(reverse_string(word))