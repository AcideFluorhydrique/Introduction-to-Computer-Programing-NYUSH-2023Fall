"""
Exercise 2 - Perfect Numbers

A proper divisor of a positive integer N, is a positive 
integer less than N that divides evenly into N leaving 
no remainder. For example, the proper divisors of 18 
are: 1, 2, 3, 6 and 9.

Write the function proper_divisors (in the file exercise2.py) 
that does the following:


Function proper_divisors(N)
• takes 1 parameter N → type int
• returns the sum of the proper divisors of N → type int
"""
def proper_divisors(N):
    S = 0
    for i in range(1,N):
        if N % i == 0:
            S = S + i
    return S

"""
An integer, N, is said to be perfect when the sum of all 
of the proper divisors of N is equal to N. For example, 
28 is a perfect number because its proper divisors are 
1, 2, 4, 7 and 14, and 1 + 2 + 4 + 7 + 14 = 28.


Write the function perfect_number (in the file exercise2.py)
that does the following:

Function perfect_number(N)
• takes 1 parameter N → type int
• calls the function proper_divisor
• returns whether the number is a perfect number → type bool
"""

def perfect_number(N):
    s = proper_divisors(N)
    if s == N:
        return True
    else:
        return False

"""
Then, write a program ( in the main() in the file exercise2.py) 
that does the following.

Program main()
• calls the function perfect_number for numbers between 1 and 10,000
• prints out the number if it is a perfect number
"""

def main():
    for N in range (1,10001):
        if perfect_number(N):
            print(N)
main()
