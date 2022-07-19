#--------
print("ejemplo 1")
friends_age = {"Rolf": 24, "Adam": 30, "Anne": 27}
print(friends_age["Adam"])

#--------
print("ejemplo 2")
friends_age = {"Rolf": 24, "Adam": 30, "Anne": 27}
friends_age ["Bob"] = 21
print(friends_age)

#--------
print("ejemplo 3")
friends_age = {"Rolf": 24, "Adam": 30, "Anne": 27}
friends_age ["Rolf"] = 51
print(friends_age)

#--------
print("ejemplo 4")
friends = [
    {"name": "Rolf", "age": 24},
    {"name": "Adam", "age": 30},
    {"name": "Anne", "age": 27},
]
print(friends)

#--------
print("ejemplo 5")
print(friends[1])

#--------
print("ejemplo 6")
print(friends[1]["name"])

#--------
print("--- ejemplo 7 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student in student_attendance:
    print(student)

#--------
print("--- ejemplo 8 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student in student_attendance:
    print(student)

#--------
print("--- ejemplo 9 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student in student_attendance:
    print(f"{student}: {student_attendance[student]}")

#--------
print("--- ejemplo 10 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for student, attendance in student_attendance.items():
    print(f"{student}: {attendance}")

#--------
print("--- ejemplo 11 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
if "Bob" in student_attendance:
    print(f"Bob: {student_attendance['Bob']}")
else:
    print("Bob is not a student in this class")    

#--------
print("--- ejemplo 12 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}

attendance_values = student_attendance.values()
print(sum(attendance_values)/ len(attendance_values))







