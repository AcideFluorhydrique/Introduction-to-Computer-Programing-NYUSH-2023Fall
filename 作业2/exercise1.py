phase = input("Is the moon full? If yes enter Full if no enter No: ")
distance = int(input("Enter the distance of the moon from the earth: "))
date = int(input("Enter the date of the month: "))
eclipse = input("Is there an eclipse? Enter True for yes and False for no: ")
if phase == "No":
    print("Moon")
else:
    if (date == 29 or date == 30 or date ==31) and eclipse == "True" and distance < 230000:
        print("Super Blue Blood Moon")
    elif (date == 29 or date == 30 or date ==31) and eclipse == "True" and distance >= 230000:
        print("Blue Blood Moon")
    elif (date == 29 or date == 30 or date ==31) and eclipse == "False" and distance < 230000:
        print("Super Blue Moon")
    elif (date == 29 or date == 30 or date ==31) and eclipse == "False" and distance >= 230000:
        print("Blue Moon")
    elif (date != 29 and date != 30 and date !=31) and eclipse == "True" and distance < 230000:
        print("Super Blood Moon")
    elif (date != 29 and date != 30 and date !=31) and eclipse == "True" and distance >= 230000:
        print("Blood Moon")
    elif (date != 29 and date != 30 and date !=31) and eclipse == "False" and distance < 230000:
        print("Super Moon")
    else:
        print("Full Moon")