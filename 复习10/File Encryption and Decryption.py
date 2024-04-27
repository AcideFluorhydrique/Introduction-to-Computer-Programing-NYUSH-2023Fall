pc = {}
pcreverse = {}
f = open("D:\\src\\python_study\\icp\\复习10\\codes.txt","r")
content = f.readlines()
for text in content:
    p,c = (text.strip()).split(" ")
    pc[p] = c
    pcreverse[c] = p


# print(pc)
f1 = open("D:\\src\\python_study\\icp\\复习10\\uniquewords.txt")
line = f1.read()
# print(line)
encr = ""
for C in line:
    if C.isalpha():
        encr += pc[C]
    else:
        encr += C
print(encr)

# 反向破译
decr = ""
for C in encr:
    try:
        decr += pcreverse[C]
    except:
        decr += C

print(decr)



