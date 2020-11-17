import json
grades = open("grades.txt", "r")
grades_list = grades.readlines()
highest_grade = 0
name_student = ""
for i in grades_list:
    student_information = i.strip(": ").split(" ")
    if float(student_information[3]) > highest_grade :
        highest_grade = float(student_information[3])
        name_student = student_information[1]


json_file = open("grades-information.json", "w")
grades_information = {name_student: highest_grade}
json.dump(grades_information, json_file, indent=2)
