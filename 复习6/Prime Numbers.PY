"""

A prime number is a number that is only evenly divisible by itself and 1. For example, the number
5 is prime because it can only be evenly divided by 1 and 5. The number 6, however, is not prime
because it can be divided evenly by 1, 2, 3, and 6.
Write a Boolean function named is_prime which takes an integer as an argument and returns
True if the argument is a prime number, or False otherwise. Use the function in a program that
prompts the user to enter a number and then displays a message indicating whether the number is
prime.

"""

def is_prime(n):
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
        #return 自带 break 的功能
    return True

# for k in range (1, 1000):
#     print(k, is_prime(k))


for j in range(2,1000):
    if is_prime(j):
        print(j)


# import turtle
