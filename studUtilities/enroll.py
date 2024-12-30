"""
File Name: enroll.py
Purpose:
   add enrollment functions and other enrollment functionality

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import os;
import csv;
from datetime import datetime;

dataFolder = "data";
enrollFile = os.path.join(dataFolder, "enrollment.csv");
courFile = os.path.join(dataFolder, "courses.csv");
studFile = os.path.join(dataFolder, "students.csv");


def iniEnrollFile():
    #Create the enrollment file with headers if it doesn't exist.
    if not os.path.exists(enrollFile):
        with open(enrollFile, mode='w', newline='') as file:
            writer = csv.writer(file);
            # Headers must match references in enrollStudent and viewEnrollment
            writer.writerow(["studentID", "courseID", "courseName", "instructorName", "enrollDate"]);

def viewEnrollment(studId):
    #View all courses a student is enrolled in.
    iniEnrollFile();

    found = False
    print(f"Enrollments for Student ID: {studId}");
    print(f"{'courseID':<10} {'courseName':<30} {'instructorName':<30} {'enrollDate'}");
    print("-" * 80);

    with open(enrollFile, mode='r') as file:
        reader = csv.DictReader(file);
        for row in reader:
            if row["studentID"] == studId:
                found = True;
                print(f"{row['courseID']:<10} {row['courseName']:<30} {row['instructorName']:<30} {row['enrollDate']}");

    if not found:
        print("No Enrollments Found. Please Enroll in a course.");

#List all available courses from the courses file.
def listAvailableCourses():
    if not os.path.exists(courFile):
        print("Courses file not found! Please ensure it exists.");
        return [];

    courses = [];
    try:
        with open(courFile, mode='r') as file:
            reader = csv.DictReader(file);
            print("\nAvailable Courses:");
            print(f"{'CourseID':<10} {'CourseName':<30} {'InstructorName'}");
            print("-" * 60);
            for row in reader:
                courses.append(row);
                print(f"{row['courseId']:<10} {row['courseName']:<30} {row['instructorName']}");
    except FileNotFoundError:
        print("Courses file not found.");
    return courses;

#Enroll a student in a course.
def enrollStudent(studId, courId):
    iniEnrollFile();

    # Check if the course exists
    availableCourses = listAvailableCourses();
    selectedCourse = next((course for course in availableCourses if course['courseId'] == courId), None);

    if not selectedCourse:
        print(f"Invalid Course ID: {courId}. Please select a valid course.");
        return

    #Check if the student is already enrolled in the course
    with open(enrollFile, mode='r') as file:
        reader = csv.DictReader(file);
        for row in reader:
            if row["studentID"] == studId and row["courseID"] == courId:
                print(f"You are already enrolled in {selectedCourse['courseName']}.");
                return

    #Add enrollment record
    with open(enrollFile, mode='a', newline='') as file:
        writer = csv.writer(file);
        writer.writerow([
            studId,
            selectedCourse['courseId'],
            selectedCourse['courseName'],
            selectedCourse['instructorName'],
            datetime.now().strftime("%Y-%m-%d")
        ]);

    print(f"Successfully enrolled in {selectedCourse['courseName']} (Course ID: {courId}).");

