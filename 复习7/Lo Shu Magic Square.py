"""
In a program you can simulate a magic square using a two-dimensional list. Write a function that
accepts a two-dimensional list as an argument and determines whether the list is a Lo Shu Magic
Square.
"""


a = input("Enter a the fisrt line of the Figure(用逗号隔开): ").split(",")
List1 = [int(a[i]) for i in range(len(a))]

b = input("Enter a the second line of the Figure(用逗号隔开): ").split(",")
List2 = [int(b[i]) for i in range(len(b))]

c = input("Enter a the third line of the Figure(请你用逗号隔开): ").split(",")
List3 = [int(c[i]) for i in range(len(c))]


L =[List1,List2,List3]

# if L[0][0] + L[0][1] + L[0][2] != 15:
#     print(False)
# elif L[1][0] + L[1][1] + L[1][2] != 15:
#     print(False)
# elif L[2][0] + L[2][1] + L[2][2] != 15:
#     print(False)
# elif L[0][0] + L[1][0] + L[2][0] != 15:
#     print(False)
# elif L[0][1] + L[1][1] + L[2][1] != 15:
#     print(False)
# elif L[0][2] + L[1][2] + L[2][2] != 15:
#     print(False)
# elif L[0][0] + L[1][1] + L[2][2] != 15:
#     print(False)
# elif L[2][0] + L[1][1] + L[0][2] != 15:
#     print(False)
# else:
#     print(True)
def loshu(L):
    for r in L:
        if sum(r) != 15:
            return False
    
    for j in range(len(L[0])):
        s = 0
        for i in range(len(L)):
            s += L[i][j]
        if s != 15:
            return False
    left = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            # left += L[i][j]
            if i == j:
                left += L[i][j]
    if left != 15:
        return False
    right = 0
    for i in range(len(L)):
        for j in range(len(L[0])):
            if i + j == 3:
                right += L[i][j]
    if right != 15:
        return False

    return True

print(loshu(L))
    
    