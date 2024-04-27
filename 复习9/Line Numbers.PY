o = input("Plz enter the file name and the location like this: 'C:\\Users\\geora\\Desktop\\ICP 2023fall\\Training files\\numbers.txt' >>>")
f = open(o,"r")
i = 0
while True:
    line = f.readline()
    if line:
        i += 1
    else:
        break
print(i)