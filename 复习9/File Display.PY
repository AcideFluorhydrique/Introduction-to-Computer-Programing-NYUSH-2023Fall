# import os



# f = open("C:\\Users\\geora\\Desktop\\ICP 2023fall\\Training files\\numbers.txt","r")
# while True:
#     line = f.readline()
#     if line:
#         if (line.strip()).isnumeric():
#             print(line)
#     else:
#         break

"""
Another way to do so
"""

f = open("C:\\Users\\geora\\Desktop\\ICP 2023fall\\Training files\\numbers.txt","r")
while True:
    line = f.readline()
    if line:
        try:
            print(int(line))
        except ValueError:
            continue
    else:
        break
f.close()