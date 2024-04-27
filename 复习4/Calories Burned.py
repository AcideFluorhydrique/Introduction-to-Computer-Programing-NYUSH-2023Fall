"""

n=10
while n<=30:
    s= int(n *4.2)
    n=5+n
    print("You burned",s,"Calories")


"""

#then let's use for 

for i in range(30):
    if i>8 and (i+1)%5==0:
        print("You burned", 4.2*(i+1),"Calories")