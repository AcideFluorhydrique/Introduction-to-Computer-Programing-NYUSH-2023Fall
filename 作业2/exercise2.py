position = str(input("Enter a chess board position: "))
x = position[0]
y=int(position[1])
if x == "a"or x =="c"or x== "e"or x== "g":
    x=1
else:
    x=2
if (x+y)/2==(x+y)//2:
    print("This case is black")
else:
    print("This case is white")