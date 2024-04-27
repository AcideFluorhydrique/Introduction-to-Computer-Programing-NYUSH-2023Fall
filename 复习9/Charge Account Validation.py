"""
Start by downloading the data file charge accounts.txt (link). This file has a list of a com-
pany's valid charge account numbers. Each account number is a seven-digit number, such as
5658845 .

Write a program that reads the contents of the file into a list. The program should then ask
the user to enter a charge account number. The program should determine whether the number
is valid by searching for it in the list. If the number is in the list, the program should display a
message indicating the number is valid. If the number is not in the list, the program should display
a message indicating the number is invalid.

"""

f = open("C:\\Users\\geora\\Desktop\\ICP 2023fall\\Training files\\charge_accounts.txt","r")
A = []
while True:
    line = f.readline
    if line:
        A.append(line)
    else:
        break
x = (input("enter a charge account number: "))
if x in A:
    print("Valid")
else:
    print("Invalid")
f.close