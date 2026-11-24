# Concept 10: Break and Continue
print("Break example:")
for number in range(1, 6):
    if number == 4:
        break
    print(number)

print("Continue example:")
for number in range(1, 6):
    if number == 3:
        continue
    print(number)
