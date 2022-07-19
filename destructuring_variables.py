#--------
print("--- ejemplo 1 ----")
t = 5, 11
x, y = t
print(t)
print(x, y)

#--------
print("--- ejemplo 2 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
print(list(student_attendance.items()))

#--------
print("--- ejemplo 3 ----")
student_attendance = {"Rolf": 96, "Bob": 80, "Anne": 100}
for t in student_attendance.items():
    print(t)

#--------
print("--- ejemplo 4 ----")
people = [("Bob", 42, "Mechanic"),("James", 24, "Artist"),("Harry", 32, "Lecturer")]
for name, age, profession in people:
    print(f"Name: {name}, Age: {age}, Profession {profession}")

#--------
print("--- ejemplo 5 ----")
people = [("Bob", 42, "Mechanic"),("James", 24, "Artist"),("Harry", 32, "Lecturer")]
for person in people:
    print(f"Name: {person[0]}, Age: {person[1]}, Profession {person[2]}")
    
#--------
print("--- ejemplo 6 ----")
person = ("Bob", 42, "Mechanic")
name, _, profession = person
print (name, profession)

#--------
print("--- ejemplo 7 ----")
head, *tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

#--------
print("--- ejemplo 8 ----")
*head, tail = [1, 2, 3, 4, 5]
print(head)
print(tail)

#--------
print("--- ejemplo 9 ----")
*head, tail = [1, 2, 3, 4, 5]
print(*head)
print(tail)


