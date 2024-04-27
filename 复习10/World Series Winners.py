"""
Start by downloading the data file WorldSeriesWinners.txt (link). This file contains a chrono-
logical list of the World Series' winning teams from 1903 through 2016. The first line in the file is
the name of the team that won in 1903, and the last line is the name of the team that won in 2016.
(Note that the World Series was not played in 1904 or 1994. There are entries in the file indicating
this.)
Write a program that reads this file and creates a dictionary in which the keys are the names of
the teams and each key's associated value is the number of times the team has won the World
Series. The program should also create a dictionary in which the keys are the years and each key's
associated value is the name of the team that won that year.
The program should prompt the user for a year in the range of 1903 through 2016. It should then
display the name of the team that won the World Series that year and the number of times that
team has won the World Series.
"""

f = open("D:\\src\\python_study\\icp\\复习10\\WorldSeriesWinners.txt")

teams = f.readlines()
winners = {}
years = {}
y = 1903
for t in teams:
    t = t.strip()
    winners[t] = winners.get(t,0) + 1
# print(winners)
    years[str(y)] = t
    y = y + 1
print(years)
