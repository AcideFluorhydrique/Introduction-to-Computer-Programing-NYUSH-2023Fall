score=int(input("Score: "))
while score > 100 or score <0:
    print("Invalid input. Please enter a score between 0 and 100.")
    score=int(input("Score: "))
if score >= 95:
    print("Your grade is A")
elif score >= 90:
    print("Your grade is A-")
elif score >= 87:
    print("Your grade is B+")
elif score >= 83:
    print("Your grade is B")
elif score >= 80:
    print("Your grade is B-")
elif score >= 77:
    print("Your grade is C+")
elif score >= 73:
    print("Your grade is C")
elif score >= 70:
    print("Your grade is C-")
elif score >= 67:
    print("Your grade is D+")
elif score >= 63:
    print("Your grade is D")
else:
    print("Your grade is F")