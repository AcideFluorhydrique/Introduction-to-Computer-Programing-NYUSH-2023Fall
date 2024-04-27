import random
# S = ""
one = 0
two = 0
three = 0
four = 0
five = 0
six = 0
for i in range(1001):
    r = random.randint(1,6)
    if r == 1:
        one = one +1
    elif r==2:
        two += 1
    elif r==3:
        three += 1
    elif r== 4:
        four = four +1
    elif r== 5:
        five+=1
    else:
        six = six +1
print("One appears ", one, " times")
print("Two appears ", two, " times")
print("Three appears ", three, " times")
print("Four appears ", four, " times")
print("Five appears ", five, " times")
print("Six appears ", six, " times")
#     S = S +str(r)
# print(S)