def largest(arr):

    max_num = arr[0]

    for num in arr:
        if num > max_num:
            max_num = num

    return max_num

arr = [5,12,9,30,87,54,18]

print(largest(arr))