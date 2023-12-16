def proper_divisors(N):
    S = 0
    for i in range(1,N):
        if N % i == 0:
            S = S + i
    return S
def perfect_number(N):
    s = proper_divisors(N)
    if s == N:
        return True
    else:
        return False
def main():
    for N in range (1,10001):
        if perfect_number(N):
            print(N)
main()



# def proper_divisors(N):
#     divisors = [i for i in range(1, N) if N % i == 0]
#     return sum(divisors)

# def perfect_number(N):
#     return N == proper_divisors(N)

# def main():
#     for i in range(1, 10001):
#         if perfect_number(i):
#             print(i)

# main()