"""
File Name: adminUtil.py
Purpose:
   admin utility file

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import csv;
from userClass import User;
from adminClass import Admin;

def loadAdmin(csvFile):
    admins = {}
    try:
        with open(csvFile, mode='r') as file:
            reader = csv.DictReader(file)
            for row in reader:
                admins[row['userName']] = Admin(row['userName'], row['passWord'])
    except FileNotFoundError:
        print(f"Error: {csvFile} not found.")  # Error Handling
    return admins

def authUser(admins):
    attempts = 0
    maxAttempts = 5

    while attempts < maxAttempts:
        username = input("Please enter your username: ").strip()
        password = input("Please enter your password: ").strip()

        if username in admins and admins[username].authenticate(password):
            print("Authentication successful! Welcome!")
            return admins[username]
        else:
            attempts += 1
            print(f"Incorrect username or password. Attempts left: {maxAttempts - attempts}")

    print("Maximum attempts reached. Exiting.")
    return None

def landingPage(admin):
    while True:
        print("\nAdmin Menu:")
        print("1. Add Instructor")
        print("2. Add Student")
        print("3. Add Course")
        print("4. View Menu")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ").strip()

        if choice == '1':
            admin.addInstructor()
        elif choice == '2':
            admin.addStudent()
        elif choice == '3':
            admin.addCourse()
        elif choice == '4':
            print("\nViewing Menu:")
            print("1. View Courses")
            print("2. View Instructors")
            print("3. View Students")
            print("4. View Enrollments")
            print("5. Back")

            sub_choice = input("Enter your choice (1-5): ").strip()
            if sub_choice == '1':
                admin.viewCourse()
            elif sub_choice == '2':
                admin.viewInstructors()
            elif sub_choice == '3':
                admin.viewStudents()
            elif sub_choice == '4':
                admin.viewEnrollment()
            elif sub_choice == '5':
                continue
        elif choice == '5':
            print("Exiting. Bye!")
            break
        else:
            print("Invalid choice. Please try again.")  #Error Handling

def main():
    csvFile = "adminInfo.csv"
    admins = loadAdmin(csvFile)

    if not admins:
        print("No Admin info loaded. Exiting.")     #error handling
        return

    authAdmin = authUser(admins)
    if authAdmin:
        landingPage(authAdmin)

if __name__ == "__main__":
    main()
        

