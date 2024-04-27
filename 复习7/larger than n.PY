n = int(input("Plz enter a number: "))
a = input("Enter a 列表(用逗号隔开): ").split(",")
List = [int(a[i]) for i in range(len(a))]
b = []
for i in List:
    if i > n:
        b.append(i)
print(b)