"""
year = 1
tuition = 8000
while year <= 5:
    print("The tuition fee in year {} is ${}".format(year,tuition))
    year = year +1
    tuition = tuition * 1.03
"""
#For loops

tuition = 8000
for year in range(1,6):
    print("The tuition fee in year {} is ${}".format(year,tuition))
    tuition = tuition * 1.03