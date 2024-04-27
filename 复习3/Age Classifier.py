x=int(input('What is your age??'))
if x <= 1:
    print("infant")
elif 1<x and x<13:
    print("child")
elif x>=13 and x<20:
    print("teenager")
else:
    print("adult")