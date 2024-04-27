"""
Assume that hot dogs come in packages of 10, and hot dog buns come in packages of 8.
Write a program that calculates the number of packages of hot dogs and the number of packages
of hot dog buns needed for a cookout, with the minimum amount of leftovers.
The program should ask the user for the number of people attending the cookout and the number
of hot dogs each person will be given.
The program should display the following details:
• The minimum number of packages of hot dogs required
• The minimum number of packages of hot dog buns required
• The number of hot dogs that will be left over
• The number of hot dog buns that will be left over
"""
peoplenumber=int(input("How many people?? "))
eachpersonwant=int(input("How many hot dogs each person want? "))
x=peoplenumber*eachpersonwant
if x//10==x/10:
    package_of_hotdogs=x/10
    print("The minimum number of packages of hot dogs required is",package_of_hotdogs)
else:
    package_of_hotdogs=1+x//10
    print("The minimum number of packages of hot dogs required is",package_of_hotdogs)
if x//8==x/8:
    package_of_hotdogs_buns=x/8
    print("The minimum number of packages of hot dogs buns required is",package_of_hotdogs_buns)
else:
    package_of_hotdogs_buns=1+x//8
    print("The minimum number of packages of hot dogs buns required is",package_of_hotdogs_buns)
hotdogsleft=10*package_of_hotdogs -x
hotdogsbunsleft = 8*package_of_hotdogs_buns -x
print("The number of hot dogs that will be left over is",hotdogsleft)
print("The number of hot dogs buns that will be left over is",hotdogsbunsleft)