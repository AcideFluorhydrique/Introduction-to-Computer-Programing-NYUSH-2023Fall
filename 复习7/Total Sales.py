a = input("Enter a 列表: ").split(",")
List = [int(a[i]) for i in range(len(a))]

b = 0
for i in List:
    b += int(i)
print(b)