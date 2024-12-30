"""
File Name: viewTeaching.py
Purpose:
   add instructor's viewteaching and other viewing functionality

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import os;
import csv;

# File paths
dataFolder = "data";
coursesFile = os.path.join(dataFolder, "courses.csv");

def loadCoursesData():
    #Load courses data to find courses taught by instructors.
    courses = [];
    try:
        with open(coursesFile, mode='r') as file:
            reader = csv.DictReader(file);
            for row in reader:
                courses.append(row);  # Append each course row as a dictionary
    except FileNotFoundError:
        print(f"Error: {coursesFile} not found.");
    return courses;

def viewTeaching(instID):
    #Display the courses taught by the instructor with the given ID.
    courses = loadCoursesData();

    if not courses:
        print("No courses found in the system.");
        return;

    # Filter courses taught by the given instructor ID
    taughtCourses = [course for course in courses if course['instructorID'] == instID];

    if not taughtCourses:
        print("You are not currently teaching any courses.");
        return

    # Display the courses in a readable format
    print("\nCourses You Are Teaching:");
    print(f"{'CourseID':<10} {'CourseName':<30} {'InstructorName'}");
    print("-" * 60);
    for course in taughtCourses:
        print(f"{course['courseId']:<10} {course['courseName']:<30} {course['instructorName']}");

    # Test logic
if __name__ == "__main__":
    # extended login logic
    instID = input("Enter your authenticated Instructor ID: ").strip();
    viewTeaching(instID);