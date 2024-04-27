"""
C=0
while C<= 20:
    F = 1.8 * C + 32
    print(C,"degree Celcius equals",F,"degree Farenheit")
    C=C+1

"""

# Then just use for loops instead of while loops

for C in range(21):
    F =round(1.8 * C + 32, 1)
    print(C,"degree Celcius equals to",F,"degree Farenheit")
