color1= input("First color")
color2= input("Second color")
if color1 == "red" and color2 == "blue" or  color1 == "blue" and color2 == "red":
    print("purple")
elif color1 == "red" and color2 == "yellow" or  color1 == "yellow" and color2 == "red":
    print("orange")
elif color1 == "yellow" and color2 == "blue" or  color1 == "blue" and color2 == "yellow":
    print("green")
else: 
    print("Error")