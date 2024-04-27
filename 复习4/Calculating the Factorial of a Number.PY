"""


x = int(input("Please enter a number: "))
y=1
z=1
factorial =1
while z < x:
    y = y + 1
    factorial = factorial * y
    z = z + 1
print("{}! = {}".format(x,factorial))
"""

#Then use for loops:

S =1 
x = int(input("Please enter a number: "))
for i in range(1,x+1):
    S = S * i
print("{}! = {}".format(x,S))
