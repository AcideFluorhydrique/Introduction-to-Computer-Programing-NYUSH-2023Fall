f = open("D:\\src\\python_study\\icp\\复习10\\uniquewords.txt")
content = (f.read()).split(" ")
processed_cont = []
for string in content:
    processed_cont += string.split("\n")

for i in range(len(processed_cont)):
    new = ""
    for c in processed_cont [i]:
        if c not in "?().,":
            new += c
    processed_cont[i] = new

for i in range(len(processed_cont)):
    if len(processed_cont[len(processed_cont) - 1 - i]) == 0:
        processed_cont.pop(len(processed_cont) - i - 1)
unique = set(processed_cont)
print(unique)

freq = {}
for w in processed_cont:
    freq[w] = freq.get(w,0) + 1

print(freq)