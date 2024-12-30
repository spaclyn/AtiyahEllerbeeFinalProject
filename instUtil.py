"""
File Name: instrUtil.py
Purpose:
   instructor Utility file

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import os;
import csv;
from userClass import User;
from instClass import Instructor;

dataFolder = "data";
instFile = os.path.join(dataFolder, "Instructors.csv");


#Function to load Instructor data
def loadInst(csvFile):
    instInfo = {};
    try:
        with open(csvFile, mode='r') as file:
            reader = csv.DictReader(file);
            for row in reader:
                instInfo[row['instID']] = row['passWord'];
    except FileNotFoundError:
        print(f"Error: {csvFile} not found.");
    return instInfo;

#Authenticate user and return an Instructor object if successful
def authUser(userInfo):
    attempts = 0;
    maxAttempts = 5;

    while attempts < maxAttempts:
        username = input("Please enter your username: ").strip();
        password = input("Please enter your password: ").strip();

        if username in userInfo and userInfo[username] == password:
            print("Authentication successful! Welcome!");
            return Instructor(username, password);  #Create and return an Instructor object
        else:
            attempts += 1
            print(f"Incorrect username or password. Attempts left: {maxAttempts - attempts}");

    print("Maximum attempts reached. Exiting.");
    return None;

#Landing page for authenticated Instructor
def landingPage(instructor):
    print("\nWelcome to the Instructor Menu!");

    while True:
        print("\nInstructor Menu:");
        print("1. View Your Courses");
        print("2. Exit");

        choice = input("Enter your choice (1-2): ").strip();

        if choice == '1':
            instructor.viewCourses();  #Call choice method
        elif choice == '2':
            print("Exiting. Bye Bye!");
            break
        else:
            print("Invalid choice. Please try again.");

def main():
    csvFile = instFile;
    instInfo = loadInst(csvFile);

    if not instInfo:
        print("No Instructor info loaded. Exiting.");
        return

    Instructor = authUser(instInfo);  #Authenticate and create an Instructor object
    if Instructor:
        landingPage(Instructor);  #Pass the Instructor object to the landing page


if __name__ == "__main__":
    main();
