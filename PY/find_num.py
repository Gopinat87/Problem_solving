def second_smallest(arr):

    smallest = float('inf')
    second = float('inf')

    for num in arr:

        if num < smallest:
            second = smallest
            smallest = num

        elif smallest < num < second:
            second = num

    if second == float('inf'):
        return -1

    return second


arr = [8,5,2,9,5,6]

print(second_smallest(arr))