import json
import os

# ---------------- STUDENT FILE ----------------

if os.path.exists("students.json"):
    with open("students.json","r") as file:
        student = json.load(file)
else:
    student = {}

def save_students():
    with open("students.json","w") as file:
        json.dump(student,file,indent=8)


# ---------------- ADMIN FILE ----------------

if os.path.exists("admins.json"):
    with open("admins.json","r") as file:
        admin = json.load(file)
else:
    admin = {}

def save_admins():
    with open("admins.json","w") as file:
        json.dump(admin,file,indent=8)


# ---------------- GRADE FUNCTION ----------------

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


# ---------------- MAIN PROGRAM ----------------

while True:

    print("\n<------STUDENT MANAGEMENT SYSTEM------>")
    print("1 -> Login as Admin")
    print("2 -> Login as Student")
    print("3 -> Exit")

    main_choice = input("Choose option (1/2/3): ")

    if main_choice == "1":

        print("\n------ ADMIN PANEL ------")
        print("1 -> Add Student")
        print("2 -> Enter Marks")
        print("3 -> View Student Result")
        print("4 -> Delete Student")
        print("5 -> Logout")

        admin_choice = input("Choose option (1/2/3/4/5): ")

        # -------- ADD STUDENT --------

        if admin_choice == "1":

            new_student_id = input("Enter the student ID: ")

            if not new_student_id.isdigit():
                print("Student ID must be in digits!")

            elif new_student_id in student:
                print("Student ID already exists!")

            else:
                student_name = input("Enter Student Name: ")
                student_department = input("Enter Student Department: ")
                student_age = input("Enter Student Age: ")

                student[new_student_id] = {
                    "student name": student_name,
                    "student department": student_department,
                    "student age": student_age,
                    "Marks": {}
                }

                save_students()
                print("Student added successfully")


        # -------- ENTER MARKS --------

        elif admin_choice == "2":

            student_id = input("Enter Student ID: ")

            if student_id not in student:
                print("Student not found!")

            else:

                maths_marks = input("Enter Maths marks: ")
                physics_marks = input("Enter Physics marks: ")
                english_marks = input("Enter English marks: ")
                social_marks = input("Enter Social Study marks: ")
                chemistry_marks = input("Enter Chemistry marks: ")

                if not (maths_marks.isdigit() and physics_marks.isdigit()
                        and english_marks.isdigit() and social_marks.isdigit()
                        and chemistry_marks.isdigit()):

                    print("Marks must be digits!")

                else:

                    student[student_id]["Marks"] = {
                        "Maths": int(maths_marks),
                        "Physics": int(physics_marks),
                        "English": int(english_marks),
                        "Social Study": int(social_marks),
                        "Chemistry": int(chemistry_marks)
                    }

                    save_students()
                    print("Marks added successfully")


        # -------- VIEW RESULT --------

        elif admin_choice == "3":

            student_id = input("Enter Student ID: ")

            if student_id not in student:
                print("Student not found!")

            else:

                marks = student[student_id]["Marks"]

                if not marks:
                    print("Marks not entered yet")
                    continue

                total_marks = sum(marks.values())
                subjects = len(marks)

                percentage = total_marks / subjects

                print("\n----------- STUDENT RESULT -----------\n")

                print(f"{'Subject':<15}{'Total':<10}{'Marks':<10}{'Grade':<10}")
                print("-"*45)

                for subject, m in marks.items():

                    g = grade(m)

                    print(f"{subject:<15}{100:<10}{m:<10}{g:<10}")

                print("-"*45)
                print("Total Marks:", total_marks)
                print("Percentage:", round(percentage,2), "%")


        # -------- DELETE STUDENT --------

        elif admin_choice == "4":

            student_id = input("Enter Student ID to delete: ")

            if student_id in student:

                del student[student_id]
                save_students()

                print("Student deleted successfully")

            else:
                print("Student not found")


        # -------- LOGOUT --------

        elif admin_choice == "5":
            continue


    elif main_choice == "2":
        print("Student login not implemented yet")


    elif main_choice == "3":
        print("Exiting program...")
        break


    else:
        print("Invalid option")