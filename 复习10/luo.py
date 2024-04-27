def is_updown(n):
  s = str(n)
  i = 0
  while i < len(s) - 1 and s[i] <= s[i+1]:
    i += 1
  j = len(s) - 1
  while j > 0 and s[j] <= s[j-1]:
    j -= 1
  return i == j
n = int(input("Enter a positive integer: "))
m = n + 1
while not is_updown(m):
  m += 1
print(f"The next updown number greater than {n} is: {m}")






for i in range(1,3):
	for j in range(1):
		for k in range(3,1,-1):
			print (i,j,k)

student = {
  'name': 'Alice',
  'age': 18,
  'gender': 'female'
}
print(student)

print(0.1 + 0.2 == 0.3)
