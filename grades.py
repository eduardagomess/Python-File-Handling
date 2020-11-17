number_students = int(input("Enter the number of students in class: "))
name_students = []
grades = []

for i in range(number_students):
    name_students.append(input("Enter the student name: "))
    grades.append(int(input("Enter the final grade: ")))

students_grades = open("students-grades.txt", "w")

[students_grades.write(name_students[i] + ": " + str(grades[i]) + "\n") for i in range(number_students)]
