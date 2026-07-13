# find factorial 
# using loop

num = int(input("Enter a number: "))

fact = 1

for i in range(1,num+1):

    fact *= i

print(f"Factorial of {num } is {fact}" )

#using recursive function

n = int(input("enter a num: "))

def fact(n):
    if n == 0 or n ==1:
        return 1
    
    return n * fact(n-1)

print("factorial of" , n ,"is " ,fact(n))