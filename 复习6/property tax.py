"""
A city collects property taxes on the assessment value of property, which is 60 percent of the
property's actual value. For example, if an acre of land is valued at $10,000, its assessment value
is $6,000. The property tax is then 72¢ for each $100 of the assessment value. The tax for the
acre assessed at $6,000 will be $43.20. Write a program that asks for the actual value of a piece of
property and calls a function computePropertyTax to calculate and display the assessment value
and property tax.

"""

def computePropertyTax(n):
    n = float(n)
    print("assessment value: $", n*0.6)
    print("property tax: $", n*0.6*0.0072)

n = input("Enter the actual value: $")
computePropertyTax(n)