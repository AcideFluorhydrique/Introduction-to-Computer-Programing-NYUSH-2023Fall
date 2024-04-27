c = 0
p = ""
while True:
    n = int(input("a number plz"))
    if p == n:
        c = c + 1
    else:
        p = n
    if c == 2:
        break
print("Done")

