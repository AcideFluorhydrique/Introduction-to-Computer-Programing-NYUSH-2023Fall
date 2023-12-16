"""
A fraction can be reduced to an equivalent fraction 
with a smaller numerator and a smaller denominator,
this is called simplifying or reducing a fraction.


Write the function greatest_common_divisor (in the file exercise1.py) 
that does the following.

Function greatest_common_divisor(n, m)
• takes 2 parameters n, m  →  type int
• returns the greatest common divisor of the two integers  →  type int
"""

def greatest_common_divisor(n,m):
    if n <= m:
        i = n 
        while i <= n:
            if n % i == 0 and m % i == 0:
                break
            else:
                i -= 1
    else:
        i = m
        while i <= n:
            if n % i == 0 and m % i == 0:
                break
            else:
                i = i - 1
    return i


# print(greatest_common_divisor(n,m))
# type(greatest_common_divisor(n,m))
# n = int(input("Enter the numerator: > "))
# m = int(input("Enter the denominator: > "))
# 测试一下 可行


"""
Write the function greatest_common_divisor (in the file exercise1.py)
that does the following.

Function reduce_fraction(n, m)
• takes 2 parameters n, m → type int that , respectively, represent the 
numerator and denominator of a fraction as its only two parameters.
• calls an other function greatest_common_divisor and use the returned 
value to reduce the fraction to its lowest terms.
• returns the numerator and denominator of the reduced function if the 
function can be reduced or the original numerator and denominator if 
the function cannot be reduced  →  type int
"""

def reduce_fraction(n,m):
    a = greatest_common_divisor(n,m)
    N = int(n/a)
    M = int(m/a)
    c = str(N)+"/"+str(M)
    return c

def main():
    n = int(input("Enter the numerator: > "))
    m = int(input("Enter the denominator: > "))
    if greatest_common_divisor(n,m) == 1:
        print("The fraction {}/{} cannot be reduced".format(n,m))
    else:
        x = reduce_fraction(n,m)
        print("The fraction {}/{} can be reduced to".format(n,m),x)
# 这样应该可以的
main()