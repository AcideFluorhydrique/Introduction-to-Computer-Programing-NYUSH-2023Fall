#A cookie recipe calls for the following ingredients:
#• 1.5 cups of sugar
#• 1 cup of butter
#• 2.75 cups of flour
#The recipe produces 48 cookies with this amount of the ingredients.
#Write a program that asks the user how many cookies he or she wants to make, and then displays
#the number of cups of each ingredient needed for the specified number of cookies.
cookieamount=int(input("How many cookies do you want? >>>"))
print("You need",cookieamount*1.5/48,"cups of sugar,",cookieamount/48,"cups of butter and",cookieamount*2.75/48,"cups of flour")