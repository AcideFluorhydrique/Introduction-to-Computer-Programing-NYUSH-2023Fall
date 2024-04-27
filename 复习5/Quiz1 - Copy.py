'''
Predict the output
'''
#1
print("#"*8+"1"+"#"*8)
try:
    a = 15
    b = 5
    c = 3
    print(a/(a-b*c))
except ZeroDivisionError:
    print("ZeroDivisionError: division by zero")

#2
print("#"*8+"2"+"#"*8)
a = -1 ** 2
print(a)

#3
print("#"*8+"3"+"#"*8)
x = "Hello! Nice Day!"
print(x[7:9] + x[6] + x[0] + x[-3] + x[4:6])

#4
print("#"*8+"4"+"#"*8)
a = 0
b = 1
while a < 10:
    print(a)
    c, a = a, b
    b = c + b

#5
print("#"*8+"5"+"#"*8)
x = 1
while x < 7:
    if x % 2 == 0:
        print(x, 'is even')
    else:
        print(x, 'is odd')
    x = x + 1

'''
Boolean Conditions

Assuming that: x = "even", y = "odd", z = "zero";
evaluate the following Boolean expressions.
'''
x = "even"
y = "odd"
z = "zero"

#6
print("#"*8+"6"+"#"*8)
flag = x == "even"
print(flag)

#7
print("#"*8+"7"+"#"*8)
flag = z[-1] + "d" + y[1] != y
print(flag)

#8
print("#"*8+"8"+"#"*8)
flag = (x < y) and (y < z)
print(flag)

#9
print("#"*8+"9"+"#"*8)
flag = x[5:2] == y[5:2]
print(flag)

'''
Binary Representation

The following questions contain positive integers represented in binary (8 bits) or in decimal forms.
Convert the values.
'''
#10
print("#"*8+"10"+"#"*8)
print(int(0b10010001))

#11
print("#"*8+"11"+"#"*8)
print(bin(254))

'''
Programming Exercises

You've just been hired by a party planning partnership called Party People Plus (whew, that's a lot of p's). They would like you to
write a program that prints out numbers in a count down based on a value entered by the program's user.

The program should do the following:
a) ask the user for number (and store the number entered) by saying: "How long before the party!?"
b) print out: "Here's the count down!"
c) count down from the number entered to 1 by printing out each number
d) if the current number in the countdown is less than or equal to three, surround the number with asterisks
e) at the end of the countdown, print out: "Party Time!!!"

Example Output:
How long before the party!?
> 5
Here's the count down!
5
4
*3*
*2*
*1*
Party Time!!!
'''
#12
print("#"*8+"12"+"#"*8)
num = int(input("How long before the party!?\n"))
print("Here's the count down!")
for i in range(num,0,-1):
    if i<=3:
        print(f"*{i}*")
    else:
        print(i)
print("Party Time!!!")