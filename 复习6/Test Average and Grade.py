"""
Write a program that asks the user to enter five test scores. 
The program should display a letter grade for each score and the average test score. 
Write the following functions in the program:


• calc_average - This function should accept five test scores 
as arguments and return the average of the scores.


• determine_grade - This function should accept a test score as an argument and 
return a letter grade for the score based on the following grading scale:

"""


def determine_grade(n):
    if n > 89 :
        g = 'A'
    elif n > 79 and n <= 89:
        g ="B"
    elif n > 69 and n <= 79:
        g ="C"
    elif n > 59 and n <= 69:
        g ="D"
    elif n <= 59:
        g ="F"
    print(g)

def calc_average(a,b,c,d,e):
    ave = (a + b + c + d + e)/5
    print(f"Your average score is {ave}")

a = int(input("Your first score: "))
b = int(input("Your second score: "))
c = int(input("Your third score: "))
d = int(input("Your fourth score: "))
e = int(input("Your fifth score: "))

calc_average(a,b,c,d,e)

determine_grade(a)
determine_grade(b)
determine_grade(c)
determine_grade(d)
determine_grade(e)