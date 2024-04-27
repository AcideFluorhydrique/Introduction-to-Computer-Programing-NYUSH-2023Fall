# 0 1 1 2 3 5 8 13 ……

a = 0
b = 1
n=int(input("Please enter a number: "))
for i in range(1,n+1):
    if i == 1:
        c = 0
        print(c)
    elif i ==2:
        c=1
        print(c)
    else:
        c = a + b
        print(c)
        a = b
        b=c
