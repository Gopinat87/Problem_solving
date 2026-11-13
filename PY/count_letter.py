text = "banana"

count = {}

for letter in text:
    if letter in count:
        count[letter] += 1
    else:
        count[letter] = 1
print(count)

