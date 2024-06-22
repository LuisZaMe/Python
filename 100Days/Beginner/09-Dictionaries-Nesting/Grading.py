student_grades = {
    "Harry" : 81,
    "Ron": 78,
    "Hermione": 99,
    "Draco": 74,
    "Neville": 62,
}

for student in student_grades:
    score = student_grades[student]
    if score > 91:
       student_grades[student] = "OutStanding"
    elif score > 80:
       student_grades[student] = "Exceeds Expectations"
    elif score > 70:
       student_grades[student] = "Acceptable"
    else:
       student_grades[student] = "Fail"

print(student_grades)