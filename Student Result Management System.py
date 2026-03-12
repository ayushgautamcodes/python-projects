import json 
import os

if os.path.exists("students.json"):
    with open("students.json","r") as file:
        student = json.load(file)
else:
    student ={}

def save_students ():
    with open("students.json", "w") as file:
        json.dump(student,file, indent = 8)

if os.path.exists("admins.json"):
    with open("admins.json","r") as file:
        admin = json.load(file)
else:
    admin ={}

def save_admins ():
    with open("admins.json", "w") as file:
        json.dump(admin,file, indent = 8)


while True:
    print("\n<------STUDENT MANAGEMENT SYSTEM------>")
    print("1-> Login as a Admin")
    print("2-> Login as a Student.")
    print("3-> Exite")
    main_choice = int(input("choose the option (1/2/3): "))

    if main_choice == 1:
        print("\n------ ADMIN PANEL ------")
        print("1 -> Add Student")
        print("2 -> Enter Marks")
        print("3 -> View Student Result")
        print("4 -> Delete Student")
        print("5 -> Logout")
        admin_choice = int(input("Choose option (1/2/3/4/5): "))
        
        if admin_choice == 1:
            new_student_id = input("Enter the student ID: ")

            if not new_student_id.isdigit():
                print("Student ID must be in Digits!")
            elif new_student_id in student:
                    print("Student ID is already exist!")
            else:
                student_name = input("Enter the Student Name: ")
                student_department = input("Enter the Student Department: ")
                student_age = input("Enter the Student Age: ")
                student[new_student_id] = {
                    "student name":(student_name),
                    "student department":(student_department),
                    "student age":(student_age),
                    "Marks":{}
                    }
                save_students()
                print("Student added successfully")
                
        elif admin_choice == 2:
            while True:
                print("1 -> Enter the Student Marks: ")
                print("2 -> Exit")
                admin_sub1_choice = int(input("Choose option(1/2)"))

                if admin_sub1_choice == 1:
                    while True:
                        maths_marks = (input("Enter the Maths marks: "))
                        if not maths_marks.isdigit():
                            print("Student Marks must be in Digits!")
                        else:
                            student[new_student_id]["Marks"].append(f"Maths marks: {maths_marks}")

                        physics_marks = (input("Enter the Physics marks: "))
                        if not physics_marks.isdigit():
                            print("Student Marks must be in Digits!")
                        else:
                            student[new_student_id]["Marks"].append(f"Physics marks: {physics_marks}")

                        english_marks = (input("Enter the English marks: "))
                        if not english_marks.isdigit():
                            print("Student Marks must be in Digits!")
                        else:
                            student[new_student_id]["Marks"].append(f"English marks: {english_marks}")

                        social_study_marks = (input("Enter the Social Study marks: "))
                        if not social_study_marks.isdigit():
                            print("Student Marks must be in Digits!")
                        else:
                            student[new_student_id]["Marks"].append(f"Social Study Marks: {social_study_marks}")

                        Chemistry_marks = (input("Enter the Chemistry marks: "))
                        if not Chemistry_marks.isdigit():
                            print("Student Marks must be in Digits!")
                        else:
                            student[new_student_id]["Marks"].append(f"Chemistry marks: {Chemistry_marks}")
                        save_students()
                        break

                elif admin_sub1_choice == 2:
                    break
        elif admin_choice == 3:
            print("\n----------- STUDENT RESULT -----------\n")
            marks = student[new_student_id]["Marks"]

            total_marks = sum(marks.values())
            subjects = len(marks)

            percentage = total_marks / subjects

            def grade(marks):
                if marks >= 90:
                    return "A+"
                elif marks >= 80:
                    return "A"
                elif marks >= 70:
                    return "B"
                elif marks >= 60:
                    return "C"
                elif marks >= 50:
                    return "D"
                else:
                    return "F"

            print(f"{'Subject':<15}{'Total':<10}{'Marks':<10}{'Percent':<12}{'Grade':<10}")
            print("-"*60)

            for subject, marks in student[new_student_id]["Marks"].items():
    
                percent = marks   # because total is 100
                g = grade(marks)

                print(f"{subject:<15}{100:<10}{marks:<10}{percent:<12}{g:<10}")