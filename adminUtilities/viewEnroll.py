"""
File Name: viewEnroll.py
Purpose:
   adds view enrollment and other enrollment functionality

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import os;
import csv;

#FILE PATHS
dataFolder = "data";
enrollFile = os.path.join(dataFolder, "enrollment.csv");
courFile = os.path.join(dataFolder, "courses.csv");
studFile = os.path.join(dataFolder, "students.csv");

#Create the enrollment file with headers if it doesn't exist.
def iniEnrollFile():
    if not os.path.exists(enrollFile):
        with open(enrollFile, mode='w', newline='') as file:
            writer = csv.writer(file);
            # Headers must match references in enrollStudent and viewEnrollment
            writer.writerow(["studentID", "courseID", "courseName", "instructorName", "enrollDate"]);

#Display all enrollment records
def viewAllEnrollments():

    iniEnrollFile();  # Ensure the file exists

    if not os.path.exists(enrollFile):
        print("Enrollment file not found!");
        return;

    with open(enrollFile, mode='r') as file:
        reader = csv.DictReader(file);
        enrollments = list(reader);

        if not enrollments:
            print("No enrollment records found.");
            return;

        print("\nAll Enrollment Records:");
        print(f"{'studentID':<12} {'courseID':<10} {'courseName':<30} {'instructorName':<20} {'enrollDate'}")
        print("-" * 80);

        for row in enrollments:
            print(f"{row['studentID']:<12} {row['courseID']:<10} {row['courseName']:<30} {row['instructorName']:<20} {row['enrollDate']}");
