text = "aabbcdeff"

for char in text:

    if text.count(char) == 1:
        print("First non-repeating character:", char)
        break