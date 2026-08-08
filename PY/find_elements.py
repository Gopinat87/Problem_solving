def common_elements(arr1, arr2):

    set1 = set(arr1)
    result = []

    for num in arr2:
        if num in set1 and num not in result:
            result.append(num)

    return result


arr1 = [1, 2, 3, 4, 5]
arr2 = [3, 4, 5, 6, 7]

print(common_elements(arr1, arr2))