X=float(input("Enter a number: "))
Y = X/2
while (Y**2 - X) >= 0.001 or (Y**2 - X) <= -0.001:
    Y = (Y + X/Y)/2
print("Square root:","%.3f"%Y)