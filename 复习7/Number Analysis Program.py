import random

a = []
for i in range(20):
    x = random.randint(1,100)
    a.append(x)

print(a)
total = sum(a)
maximum = max(a)
minimum = min(a)
average = total/len(a)

print("total:",total)
print("max:",maximum)
print("min:",minimum)
print("ave:",average)