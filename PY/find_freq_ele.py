numbers = [1, 2, 3, 2, 4, 2, 5, 3]

frequency = {}

for num in numbers:

    if num in frequency:
        frequency[num] += 1

    else:
        frequency[num] = 1

most_frequent = max(frequency, key=frequency.get)

print("Most frequent element:", most_frequent)
print("Frequency:", frequency[most_frequent])