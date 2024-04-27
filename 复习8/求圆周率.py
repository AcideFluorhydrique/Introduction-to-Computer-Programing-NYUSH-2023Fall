import math
# Guass-Legendre法
def gauss_legendre_pi(n):
    a = 1
    b = 1 / math.sqrt(2)
    t = 1 / 4
    p = 1
    for i in range(n):
        a1 = (a + b) / 2
        b1 = math.sqrt(a * b)
        t1 = t - p * (a - a1) ** 2
        p1 = 2 * p
        a = a1
        b = b1
        t = t1
        p = p1
    pi = (a + b) ** 2 / (4 * t)
    return pi

print(gauss_legendre_pi(1000))
