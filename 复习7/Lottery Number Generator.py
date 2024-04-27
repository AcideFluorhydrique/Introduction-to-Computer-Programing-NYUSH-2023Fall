import random
# random.randint(0,9)

def generator():
    n = ""
    for j in range(7):
        m = random.randint(0,9)
        if j == 0:
            while m == 0:
                m = random.randint(0,9)
        n += str(random.randint(0,9))
    return int(n)

def main():
    nums=[]
    for i in range(7):
        n = generator()
        nums.append(n)
    
    for e in nums:
        print(e)

main()