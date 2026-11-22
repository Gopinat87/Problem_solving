# Find the second largest unique number without sorting.

numbers = [10, 25, 5, 40, 30, 40]

largest = float("-inf")
second = float("-inf")

for num in numbers:
    if num > largest:
        second = largest
        largest = num
    elif num > second and num != largest:
        second = num

if second == float("-inf"):
    print("There is no second largest unique number.")
else:
    print("Second largest:", second)
