year = int(input("Year: "))
if (year//4 == year/4 and year//100 != year/100) or year//400 == year/400:
    print("Leap year")
else:
    print("Not leap year")
if year >= 1960 and year//4 == year/4:
    print("Euro Cup year")
if year >= 1950 and (year+2)//4 == (year+2)/4:
    print("World Cup year")