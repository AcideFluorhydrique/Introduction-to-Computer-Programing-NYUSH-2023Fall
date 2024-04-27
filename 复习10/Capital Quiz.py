"""
Write a program that creates a dictionary containing the Chinese provinces as keys and their
capitals as values. (See table below or parse file chinese-provincial-capitals.txt (link) The
program should then randomly quiz the user by displaying the name of a province and asking the
user to enter that province's capital. The program should keep a count of the number of correct
and incorrect responses.

"""

import random
f = open("D:\\src\\python_study\\icp\\复习10\\chinese-provincial-capitals.txt","r")
content = f.readlines()
pc = {}
for line in content[1:]:
    p,c = (line.strip()).split(",")
    pc[p] = c
# print(pc)

ps=[]
for k in pc.keys():
    ps.append(k)
#或者
#ps = list(pc.keys())
correct = 0
wrong = 0
while True:
    P = random.choice(ps)
    print(f"What is the capital of {P}?")
    C = input(">>>")
    
    if pc[P] == C:
        print("Correct")
        correct += 1
    else:
        print("Wrong!")
        wrong = 1 + wrong
