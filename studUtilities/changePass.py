"""
File Name: changPass.py
Purpose:
   adds student password change functionality. thought it would be cool

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import os;
import csv;

# File paths
dataFolder = "data";
studFile = os.path.join(dataFolder, "students.csv");

def changePassword(studentID):
    #Allow a student to change their password.
    try:
        #Load Students
        students = [];
        with open(studFile, mode='r') as file:
            reader = csv.DictReader(file);
            students = list(reader);

        #Parse For Student
        studFound = False;
        for student in students:
            if student['studentID'] == studentID:
                studFound = True
                print("Authenticated! You can now change your password.");
                
                #New Pass Word
                while True:
                    newPass = input("Enter your new password: ").strip();
                    if " " not in newPass:
                        break; #exit loop if no whitespace
                    else:
                        print("Input cannot contain spaces. Try again.");
                confPass = input("Confirm your new password: ").strip();
                
                if newPass == confPass:
                    student['passWord'] = newPass
                    print("Password updated successfully!");
                else:
                    print("Passwords do not match. Please try again.");     #error handling
                    return

        if not studFound:
            print("Student ID not found. Cannot change password.");
            return

        #REWRITES FILE!!!!!
        with open(studFile, mode='w', newline='') as file:
            fieldnames = ['studentID', 'firstName', 'lastName', 'passWord'];
            writer = csv.DictWriter(file, fieldnames=fieldnames);
            writer.writeheader();
            writer.writerows(students);

    except FileNotFoundError:
        print(f"Error: {studFile} not found.");             #error handling
    except Exception as e:
        print(f"An unexpected error occurred: {e}");        #error handling
