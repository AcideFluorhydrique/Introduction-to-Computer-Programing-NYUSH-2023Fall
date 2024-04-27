"""


v = float(input("What is the speed of the vehicle in kph? "))
t = int(input("How many hours has it travelled? "))
T=1
print("Hour{:<8}Distance Travelled".format(""))
while T<=t:
    print("{:^5}{:^30}".format(T,v*T))
    T=T+1
"""

#let's use for loops


v = float(input("What is the speed of the vehicle in kph? "))
t = int(input("How many hours has it travelled? "))
print("Hour{:<8}Distance Travelled".format(""))
for T in range(1,t+1):
    print("{:^5}{:^30}".format(T,v*T))
