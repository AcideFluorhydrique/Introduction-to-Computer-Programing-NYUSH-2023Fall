import random
x = input('How many random numbers are u gonna input??')
f = open("random numbers.txt","w")
for i in range(int(x)):
    f.write(str(random.randint(1,500))+"\n")
f.close()