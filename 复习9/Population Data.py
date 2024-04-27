f = open("C:\\Users\\geora\\Desktop\\ICP 2023fall\\Training files\\USPopulation.txt","r")
pop = f.readlines()
for i in range(len(pop)):
    pop[i] = int(pop[i])
# print(pop)
diff = []
for j in range(1,len(pop)):
    diff.append(pop[i]-pop[i-1])
Maxidx = diff.index(max(diff)) + 1951
Mininx = diff.index(min(diff)) + 1951
print(Maxidx,Mininx)