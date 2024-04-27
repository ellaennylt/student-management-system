# TAN YEE LING
# TP074407
# This was submitted as an assignment to CT088-0-M Programming in Python @ APU


student_masterlist = []
student_masterlist_labels = ["Student Name", "Student ID", "Course Enrolled", "Student's CGPA"]


def ask_student_name():
    # user input validation for student's name
    while True:
        student_name = input("Please enter the Student Name: ")
        names = student_name.split()
        nospace_student_name = student_name.replace(' ', '')
        if len(names) == 2 and nospace_student_name.isalpha():
            student_name = student_name.upper()
            return student_name
        else:
            print("\nThe name should only consist of first name and last name, and letters. Please re-enter.")
# function to get student name
# assumption: student name only has first name and last name
# if more than 2 names such as the inclusion of a middle/maiden name,
# user has to combine them with the last name
# assumption: all student names are unique as the name will be used as their primary identifier in the system
# rather than using the student ID, it is more intuitive for users to search and manage students based on their names


def ask_student_id():
    # validation for student's ID
    while True:
        student_id = input("Please enter the Student ID: TP")
        if len(student_id) == 6 and student_id.isdigit():
            student_id = "TP" + student_id
            return student_id
        else:
            print("\nThe ID should only contain 6 whole numbers. Please re-enter.")
# function to get student ID
# assumption: student is a student of Asia Pacific University which uses an ID that starts with TP followed by 6 digits


def ask_student_course():
    # validation for student's course
    while True:
        student_course = input("Please enter the Student's Course: ")
        if len(student_course) > 0:
            student_course = student_course.upper()
            return student_course
        else:
            print("\nThe course enrolled should not be blank. Please re-enter.")
# function to get student course
# assumption: student course can include numbers as there may be courses with numbers in the course title
# example of the above: CSC101: Introduction to Computer Science
# assumption: student can enroll in multiple courses
# both the above are to allow the system to accurately identify and manage courses,
# preventing errors and ensure data integrity


def ask_student_cgpa():
    # validation for student's CGPA
    while True:
        student_cgpa = input("Please enter the student's CGPA: ")
        try:
            student_cgpa = round(float(student_cgpa), 2)
            if 0.00 <= student_cgpa <= 4.00:
                return student_cgpa
            else:
                print("\nThe CGPA value should only be between 0.00 to 4.00. Please re-enter.")
        except ValueError:
            print("\nThe CGPA value should only be between 0.00 to 4.00. Please re-enter.")
# function to get student CGPA
# assumption: grading system follows Asia Pacific University's CGPA grading system


def view_input_details(student_name, student_id, student_course, student_cgpa):
    # printing student records for viewing and checking during registration into system
    while True:
        print("")
        print("Student Name:", student_name)
        print("Student ID:", student_id)
        print("Course Enrolled:", student_course)
        print("Student's CGPA:", "{:.2f}".format(student_cgpa))
        user_check = input("Are the details above correct? (YES/NO): ")
        # validation for user's answer
        if user_check.upper() == "YES":
            # append confirmed details into the student_masterlist
            student_masterlist.append([student_name, student_id, student_course, student_cgpa])
            print("\nThank you for the confirmation. The student has been registered.")
            print("Returning to the main menu.\n")
            mainMenu()
            break
        elif user_check.upper() == "NO":
            # prompt user to re-enter the correct student details
            print("\nPlease re-enter with the correct details.")
            student_name = ask_student_name()
            student_id = ask_student_id()
            student_course = ask_student_course()
            student_cgpa = ask_student_cgpa()
        else:
            print("\nPlease type YES or NO.")
# function to view user input details
# assumption: when user replies that the details they've provided are not correct,
# they will be prompted to fill in all the details
# this is to ensure that all details entered into the system will be
# valid, consistent, standardised, complete and error-free
# thus the choice to select a specific detail to modify was not given
# as a way to prompt the user to recheck all the details and provide the latest data


def addStudent():
    # get inputs from user on student's details
    student_name = ask_student_name()
    student_id = ask_student_id()
    student_course = ask_student_course()
    student_cgpa = ask_student_cgpa()

    # call view_input_details and pass the user inputs on student's details into the function
    view_input_details(student_name, student_id, student_course, student_cgpa)

    # append the confirmed student details to the student masterlist
    student_masterlist.append([student_name, student_id, student_course, student_cgpa])
# function to add a new student


def updateStudent():
    # prompts user and gets their input for the name of the student they'd like to update
    user_update = input("Enter the student's name to update their record: ").upper()
    names = user_update.split()
    nospace_student_name = user_update.replace(' ', '')
    # validation for name given
    if len(names) == 2 and nospace_student_name.isalpha():
        first_name, last_name = names
        student_record = [student for student in student_masterlist if
                          first_name == student[0].split()[0] and last_name == student[0].split()[1]]
    else:
        print("\nThe name should only consist of first name and last name, and letters. Please re-enter.")
        updateStudent()
        return
    # to determine if student record exists in system
    # if student record exists, prompt user to input new details
    if student_record:
        for student in student_record:
            print("Please enter the new details for", student[0])
            new_student_name = ask_student_name()
            new_student_id = ask_student_id()
            new_student_course = ask_student_course()
            new_student_cgpa = ask_student_cgpa()
            # append new student details into the student_masterlist
            for i in range(len(student_masterlist)):
                if student_masterlist[i] == student:
                    student_masterlist[i] = [new_student_name, new_student_id, new_student_course, new_student_cgpa]
                    break
            print("")
            print("Record for", new_student_name, "has been updated successfully.")
            print("Returning to the main menu.\n")
            mainMenu()
    # if student record does not exist, print error message and return to main menu
    else:
        print("\nStudent record does not exist.")
        print("Returning to the main menu.\n")
        mainMenu()
# function to update student record
# assumption: as above, to ensure all details are entered correctly and accurately into the system,
# the choice to select a specific detail to update was not given
# as a way to prompt the user to recheck all the details and provide the latest data


def viewAllStudents():
    # prints the list of all student records and the total number of records available
    # if there are no records, an error message will be printed
    if len(student_masterlist) == 0:
        print("Error: There are no student records.")
        print("Returning to the main menu.\n")
        mainMenu()
    else:
        student_masterlist.sort()
        for student in range(len(student_masterlist)):
            print("")
            print("Student", student + 1)
            for student_record in range(len(student_masterlist[student])):
                print(student_masterlist_labels[student_record] + ":", student_masterlist[student][student_record])
        print("\nTotal student records available:", student + 1)
        print("Returning to the main menu.\n")
        mainMenu()
# function to view all student records
# assumption: user only wants to view all records and perform no other action
# other functions such as searching for a specific student or updating student details
# will be performed after returning to the main menu


def user_search_again():
    # checks if user wants to search for another student
    while True:
        search_input = input("Do you want to search for another student? (YES/NO): ")
        if search_input.upper() == "YES":
            searchStudent()
        elif search_input.upper() == "NO":
            print("\nReturning to the main menu.\n")
            mainMenu()
            break
        else:
            print("\nPlease type YES or NO.")
# function to get user input to search for another student


def searchStudent():
    # prompts user and gets their input for the name of the student they'd like to search
    user_search = input("Enter the student's full name: ").upper()
    names = user_search.split()
    nospace_student_name = user_search.replace(' ', '')
    # validation for the name given
    if len(names) == 2 and nospace_student_name.isalpha():
        first_name, last_name = names
        student_record = [student for student in student_masterlist
                          if first_name == student[0].split()[0] and last_name == student[0].split()[1]]
    else:
        print("\nThe name should only consist of first name and last name, and letters. Please re-enter.")
        searchStudent()
        return
    # to determine if student record exists in system
    if student_record:
        for student in student_record:
            print("\nStudent record found as shown below.")
            for label in range(len(student)):
                print(student_masterlist_labels[label] + ":", student[label])
    else:
        print("\nStudent record does not exist.")
    user_search_again()
# function to search for student record in the system
# assumption: it is more intuitive for users to search and manage students based on their names
# assumption: all data entered into the system will be valid and error-free
# thus an accurate full name is required to search for a student and display student records


def deleteStudent():
    # prints a list of the names of all registered students in system
    print("Current list of all registered students:")
    for student in student_masterlist:
        print(student[0])
    # prompts user and gets their input for the name of the student they'd like to delete
    while True:
        user_delete = input("Enter the student's name to delete their record: ").upper()
        names = user_delete.split()
        nospace_student_name = user_delete.replace(' ', '')
        # validation for name given
        if len(names) == 2 and nospace_student_name.isalpha():
            # to determine if student record exists in system
            for student in student_masterlist:
                # if student record exists, delete student record
                if user_delete == student[0]:
                    student_masterlist.remove(student)
                    print("\nThe student's record has been deleted.")
                    print("Returning to the main menu.\n")
                    mainMenu()
            # if student record does not exist, print message and return to main menu
            else:
                print("\nStudent record does not exist.")
                print("Returning to the main menu.\n")
                mainMenu()
        else:
            print("\nThe name should only consist of first name and last name, and letters. Please re-enter.")
# function to remove student record from the system
# assumption: it is more intuitive for users to search and manage students based on their names
# assumption: all data entered into the system will be valid and error-free
# thus an accurate full name is required to delete student records


def mainMenu():
    # prints main menu display
    print("********************")
    print("Main Menu")
    print("1. Add Student")
    print("2. Update Student")
    print("3. List All Students")
    print("4. Search Student")
    print("5. Remove Student")
    print("6. Exit")
    print("********************")
    # prompts user and gets their input for the menu option number and validate the menu option number
    while True:
        try:
            menu_option = int(input("Enter your choice: "))
            if menu_option == 1:
                print("You have chosen to add a student.\n")
                addStudent()
            elif menu_option == 2:
                print("You have chosen to update a student's details.\n")
                updateStudent()
            elif menu_option == 3:
                print("You have chosen to view a list of all the students and their information.\n")
                viewAllStudents()
            elif menu_option == 4:
                print("You have chosen to search for a student.\n")
                searchStudent()
            elif menu_option == 5:
                print("You have chosen to remove a student.\n")
                deleteStudent()
            elif menu_option == 6:
                print("Exiting the Student Management System.\n")
                print("Thank you and have a good day!")
                raise SystemExit
            else:
                raise ValueError
        except ValueError:
            print("\nYou have entered an invalid option.")
            print("Please select a menu option from 1 to 6.")
# function to display main menu


mainMenu()
