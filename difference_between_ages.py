from datetime import date, datetime

current_date = datetime.strptime(str(date.today()), '%Y-%m-%d').date()

fileName1 = input("Enter file name: ")
fileName2 = input("Enter the second file name: ")

file1 = open(fileName1 + ".txt", "a")
register = "yes"

while register != "no":
    name = input("Enter your name: ")
    file1.write(name + ";")
    birthday = input("Enter your birthday: ")
    file1.write(birthday + "\n")
    register = input("Do you want to continue? yes or no: ")

file1 = open(fileName1 + ".txt", "r")

for line in file1:
    line = line.strip()
    personal_data = line.split(";")
    date_of_birthday = datetime.strptime(personal_data[1], '%d/%m/%Y').date()
    number_of_days = abs((current_date - date_of_birthday).days)
    if number_of_days/365 < 18:
        information = personal_data[0] + ": underage"
    elif number_of_days/365 >= 18:
        information = personal_data[0] + ": over 18"
    file2 = open(fileName2 + ".txt", "a")
    file2.write(information + "\n")
