"""
This exercise assumes you have completed Programming Exercise 3, Random Number File Writer.
Write another program that reads the random numbers from the file, display the numbers, and
then display the following data:
• The number of random numbers read from the file
• The sum total of the numbers
• The average of the numbers


Your program must handle the following exceptions:
• any IOError exceptions that are raised when the file is opened and data is read from it,
• any ValueError exceptions that are raised when the items that are read from the file are
converted to a number.

"""


f = open("D:\\src\\python_study\\icp\\random numbers.txt","r")
i = 0
while True:
    line = f.readline()
    if line:
        i += 1
    else:
        break
print("The number of random numbers read from the file:",i)
# 数字总数是 i
f = open("D:\\src\\python_study\\icp\\random numbers.txt","r")
S = 0
while True:
    line = f.readline()
    if line:
        try:
            line = f.readline()
            S += int(line)
        except:
            continue
    else:
        break
f.close()
print("The sum total of the numbers:",S)
print("The average of the numbers:",S/i)