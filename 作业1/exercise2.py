first_grade=int(input("1st grade: "))
second_grade=int(input("2nd grade: "))
third_grade=int(input("3rd grade: "))
Ave=(first_grade+second_grade+third_grade)//3
Ave2=(first_grade+second_grade+third_grade)%3
if Ave2>=2:
    ave_grade=Ave+1
else:
    ave_grade=Ave
print("Average grade:", ave_grade)