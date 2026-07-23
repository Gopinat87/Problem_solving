#count add numbers and even numbers

def count_even_odd(arr):

    even = 0
    odd = 0

    for num in arr:

        if num % 2 == 0:
            even += 1
        else:
            odd += 1

    print("Even =", even)
    print("Odd =", odd)

arr = [10,15,8,21,14]

count_even_odd(arr)