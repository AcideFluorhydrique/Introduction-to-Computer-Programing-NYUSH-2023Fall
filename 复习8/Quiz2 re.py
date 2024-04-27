#1
def foo():
    a = 6
    print(a)
b = foo()
print(b)

#2
"""
main()
def main():
    print("Hello World")
"""

#3
s = "helloworld"
s.upper()
print(s)

#4
def baz():
    global b
    b += a + 2
    return b
    b -= 3
a = 1
b = 2
c = baz()
print(b,c)

#5
def allSublists(L):
    sub = [[]]
    for e in range(len(L)):
        for j in range(len(L) - e):
            sub.append(L[e:e + j + 1])
    sub.sort
    return sub
print(allSublists([1,2,3,4,5]))

#6
def num_unique(L):
    unique = []
    for i in L:
        if i in unique:
            continue
        else:
            unique.append(i)
    return len(unique)
print(num_unique([1,2,2,3,3,3,4,4,4,5,5,6]))

#7 swap
def swap(L,a,b):
    temporary = L[a]
    L[a] = L[b]
    L[b] = temporary
    return L

"""or you can do it in this way"""

    # L[a], L[b] = L[b], L[a]
    # return L

#8 anagram
def anagram(a,b):
    A = []
    B = []
    for c in a:
        if c.isalpha():
            A.append(c)
    for c in b:
        if c.isalpha():
            B.append(c)
    # if len(A) != len(B):
    #     return False
    A.sort()
    B.sort()
    if A == B:
        return True
    else:
        return False
print(anagram("ba","ab"))

""" or you can do it in this way """

def anagram(a,b):
    A = []
    B = []
    for c in a:
        if c.isalpha():
            A.append(c)
    for c in b:
        if c.isalpha():
            B.append(c)
    if len(A) != len(B):
        return False
    alpha_1st = list("abcdefghijklmnopqrstuvwxyz")
    freq1 = [0]*26
    freq2 = [0]*26
    for i in A:
        idx = alpha_1st.index(i)
        freq1[idx] += 1
    for i in B:
        idx = alpha_1st.index(i)
        freq2[idx] += 1
    for j in range(len(freq1)):
        if freq1[j] != freq2[j]:
            return False
    return True
print(anagram("ba","ab"))

