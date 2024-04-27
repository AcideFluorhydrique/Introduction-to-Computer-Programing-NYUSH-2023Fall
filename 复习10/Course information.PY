rooms = {"CS101":"3004", "CS102":"4501","CS103":"6755","NT110":"1244","CM241":"1411"}
instructor = {"CS101":"Haynes", "CS102":"Alvarado","CS103":"Rich","NT110":"Burke","CM241":"Lee"}
times = {"CS101":"8", "CS102":"9","CS103":"10","NT110":"11","CM241":"13"}

course = input("course number:>>>")
print(f"course:{course}\nRoom:{rooms[course]}, Instructor:{instructor[course]}")