student = {
    "name": "Jose", "school": "Computing", "grades": (66, 77, 88),
    "name": "Bob", "school1": "Computing1", "grades": (55, 44, 33),
    "name": "Rolf", "school2": "Computing2", "grades": (11, 22, 99),
     }

def average_data(data):
    grades = data["grades"]
    return sum (grades) / len (grades)

def average_grade_all_students(student_list):
    total = 0
    count = 0
    for student in student_list:
        total = total + sum (student["grades"])
        count = count + len (student["grades"])
    return total / count

print (average_data(student))
print (average_grade_all_students(student))