# Check whether a string is a palindrome without slicing.

text = "madam"

left = 0
right = len(text) - 1

while left < right:
    if text[left] != text[right]:
        print("Not Palindrome")
        break

    left += 1
    right -= 1
else:
    print("Palindrome")
