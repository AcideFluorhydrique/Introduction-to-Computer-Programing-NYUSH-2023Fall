
p = float(input("What is the price of the print? >>>"))
n = int(input("How many square feet of wall space? >>>"))
def calculate_paint_volume(n):
    print("gallons of paint required: ",n/112,"g")
def calculate_labor_hours(n):
    print("hours of labor required: ", n*8/112,"h")
def calculate_paint_cost(n):
    print("cost of the paint: $", n*p/112)
def calculate_labor_cost(n):
    print("Labor charges: $", n*8*35/112)
def totalcost(n):
    print("Total cost: $", n*8*35/112 + n*p/112)
calculate_paint_volume(n); calculate_labor_hours(n); calculate_paint_cost(n)
calculate_labor_cost(n); totalcost(n)