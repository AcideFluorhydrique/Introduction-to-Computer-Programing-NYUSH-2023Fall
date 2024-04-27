import random
x = int(input("Password size? > "))
y=1
while y <= x:
    print(random.randint(0,9),end="")
    y = y + 1