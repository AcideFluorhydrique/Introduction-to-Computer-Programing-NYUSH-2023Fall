# startingnumberoforganisms = float(input("Starting number of organisms: "))
# increase_rate = input("Average daily increase: ")
# increase_rate = int(increase_rate[0:-1])/100
# day = int(input("Number of days to multiply: "))
# n=1
# m = round(startingnumberoforganisms,3)
# print("Day\tApproximate Population")
# while n <= day:
#     print(" {}\t\t{}".format(n,m))
#     m = m * (1 + increase_rate)
#     m = float(f"{m:.3f}")
#     n = n + 1

"""
下面用for loops
"""


startingnumberoforganisms = input("Starting number of organisms: ")
increase_rate = input("Average daily increase: ")
increase_rate = (int(increase_rate[0:-1]))/100
day = int(input("Number of days to multiply: "))
S = float(startingnumberoforganisms)

print("Day\tApproximate Population")
for i in range(1,day +1):
    print(" {}\t\t{}".format(i,("{:>.3f}".format(S))))
    y= float(1 + increase_rate)
    S = S * y