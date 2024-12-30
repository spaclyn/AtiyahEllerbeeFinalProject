"""
File Name: viewMenu.py
Purpose:
   the menu page for view options

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import os;
import csv;
from adminUtilities.addCour import iniCourFile;
from adminUtilities.addInst import iniInstFile;
from adminUtilities.addStud import iniStudFile;

#FILE PATHS
dataFolder = "data"
enrollFile = os.path.join(dataFolder, "enrollment.csv");
instFile = os.path.join(dataFolder, "instructors.csv");
courFile = os.path.join(dataFolder, "courses.csv");
studFile = os.path.join(dataFolder, "students.csv");

#VIEW COURSES
def main():
    iniCourFile(); #ensures the file exists 
    
    if not os.path.exists(courFile):
        print("Course file not found!");
        return;
    
    with open(courFile, mode='r') as file:
        reader = csv.DictReader(file);
        courses = list(reader);
    
    if not courses:         #error handling
            print("No course records found.");
            return;
    
    print("\nAll Enrollment Records:"); #tableups my output, thanks geeksforgeeks, learnpython
    print(f"{'courseId':<12} {'courseName':<30} {'instructorID':<30} {'instructorName':<20}");
    print("-" * 90);

    for row in courses:             #tableups my output, thanks geeksforgeeks, learnpython
            print(f"{row['courseId']:<12} {row['courseName']:<30} {row['instructorID']:<30} {row['instructorName']:<20}");

#VIEW INSTRUCTORS
def inst():
    iniInstFile(); #ensures the file exists 
    
    if not os.path.exists(instFile):
        print("Instructor file not found!");
        return;
    
    with open(instFile, mode='r') as file:
        reader = csv.DictReader(file);
        instructors = list(reader);
    
    if not instructors:         #error handling
            print("No Instructor records found.");  
            return;
    
    print("\nAll Instructor Records:"); #tableups my output, thanks geeksforgeeks, learnpython
    print(f"{'instID':<12} {'instTitle':<30} {'firstName':<20} {'lastName':<20} {'courses':<20}");
    print("-" * 100);

    for row in instructors:         #tableups my output, thanks geeksforgeeks, learnpython
            print(f"{row['instID']:<12} {row['instTitle']:<30} {row['firstName']:<20} {row['lastName']:<20} {row['courses']:<20}");

#VIEW STUDENTS
def stud():
    iniStudFile(); #ensures the file exists 
    
    if not os.path.exists(studFile):
        print("Instructor file not found!");
        return;
    
    with open(studFile, mode='r') as file:
        reader = csv.DictReader(file);
        students = list(reader);
    
    if not students:         #error handling
            print("No Student records found.");  
            return;

    print("\nAll Student Records:"); #tableups my output, thanks geeksforgeeks, learnpython
    print(f"{'studentID':<12} {'firstName':<30} {'lastName':<30} {'passWord':<20}");
    print("-" * 90);

    for row in students:             #tableups my output, thanks geeksforgeeks, learnpython
            print(f"{row['studentID']:<12} {row['firstName']:<30} {row['lastName']:<30} {row['passWord']:<20}");
