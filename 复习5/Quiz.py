string = input("Please input a string: ")
length = int(input("Please input the length of the substring: "))
s = ""
i = 0
while i <= len(string) - length:
    substring = string[i:i+length]
    i += 1
    if substring in s: 
        continue
    else:
        s = s + substring + ","    
s = s[:-1]
print(s)