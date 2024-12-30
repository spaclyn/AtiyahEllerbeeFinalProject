"""
File Name: studentUtil.py
Purpose:
   student Utility

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""
import os;
import csv;
from userClass import User;
from studClass import Student;
from studUtilities import enroll, changePass;

#FILE PATHS
dataFolder = "data";
studFile = os.path.join(dataFolder, "students.csv");

class Register(Student):
    def enrollIn(self):
        #Call the viewTeaching function for this student.
        registerForCourse(self.username);  #Use self.username from User class

#Function to load Student data
def loadStud(csvFile):
    #loads the Student File with the information, and parses the information
    studInfo = {};
    try:
        with open(csvFile, mode='r') as file:
            reader = csv.DictReader(file);
            for row in reader:
                studInfo[row['studentID']] = row['passWord'];
    except FileNotFoundError:
        print(f"Error: {csvFile} not found.");  #Error Handling for missing csv
    return studInfo;


# Authenticate user and return an Student object if successful
def authUser(userInfo):
    attempts = 0;
    maxAttempts = 5;

    while attempts < maxAttempts:
        username = input("Please enter your username: ").strip();
        password = input("Please enter your password: ").strip();

        if username in userInfo and userInfo[username] == password:
            print("Authentication successful! Welcome!");
            return Student(username, password);  #Create and return an Student object
        else:
            attempts += 1
            print(f"Incorrect username or password. Attempts left: {maxAttempts - attempts}");

    print("Maximum attempts reached. Exiting.");
    return None;

#Landing page for authenticated Student
def landingPage(student):
    print("\nWelcome to the Student Menu!");

    while True:
        print("\nStudent Menu:");
        print("1. Register for a course");
        print("2. View My Enrollment");
        print("3. Change Your Password");
        print("4. Exit");

        choice = input("Enter your choice (1-3): ").strip();

        if choice == '1':
            register = Register(student.username, student.password)
            register.enrollIn();  #Call method on Student object
        elif choice == '2':
            student.viewEnroll();  #Call method on Student object
        elif choice == '3':
            student.changePassword();  #Call method on Student object
        elif choice == '4':
            print("Exiting. Bye Bye!");
            break
        else:
            print("Invalid choice. Please try again.");

def registerForCourse(studId):
    #List available courses
    print("\nAvailable Courses:");
    enroll.listAvailableCourses();  #Displays available courses

    #Prompt student to select a course
    courId = input("\nEnter the Course ID you wish to enroll in: ").strip();
    if courId:
        enroll.enrollStudent(studId, courId);  #Attempt to enroll student in the course
    else:
        print("No Course ID entered. Returning to the menu.");


def main():
    csvFile = studFile;
    instInfo = loadStud(csvFile);

    if not instInfo:
        print("No Student info loaded. Exiting.");
        return

    Student = authUser(instInfo);  #Authenticate and create an Student
    if Student:
        landingPage(Student);  #Pass the Student to the landing page


if __name__ == "__main__":
    main();
