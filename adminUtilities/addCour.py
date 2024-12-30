"""
File Name: addCour.py
Purpose:
   add course functionality

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import csv;
import os;

#FILE PATHS
dataFolder = "data";
courFile = os.path.join(dataFolder,"courses.csv");
instFile = os.path.join(dataFolder,"instructors.csv");

#Load existing instructor IDs from the instructors file.
def loadInstIds():
    instId = set();
    try:
        with open(instFile, mode='r') as file:
            reader = csv.reader(file);
            next(reader, None);  #Skip the header row
            for row in reader:
                if row:         #Avoid processing empty rows
                    instId.add(row[0]); 
    except FileNotFoundError:
        print("Instructor file not found. Please create instructors first!");
        return instId;
    return instId;

#Load existing student IDs from the file.
def loadExistIds():
    existIds = set();
    try:
        with open(courFile, mode='r') as file:
            reader = csv.reader(file);
            next(reader, None);  #Skip the header row
            for row in reader:
                if row:  #Avoid processing empty rows
                    existIds.add(row[0]);

    except FileNotFoundError:
        #If the file doesn't exist, file assumes there is no students
        pass;
    return existIds;

def iniCourFile():
    #Ensures the courses CSV file exists with the proper header.
    if not os.path.exists(courFile):
        with open(courFile, mode='w', newline='') as file:
            writer = csv.writer(file);
            # Add headers to the CSV file
            writer.writerow(["courseId", "courseName", "instructorID", "instructorName"]);

def appendCourse(instructorId, courseID):
    #Add a course to the instructor's record.
    rows = [];
    updated = False;

    # Read the existing data, including the header
    with open(instFile, mode='r') as file:
        reader = csv.reader(file);
        headers = next(reader, None);  # Read and store the header row
        for row in reader:
            if row and row[0] == instructorId:  # Match instructor ID
                # Handle the 'courses' column
                courIndex = headers.index("courses");
                if len(row) <= courIndex:
                    row.append(courseID);  # Add 'courses' column if missing
                else:
                    row[courIndex] = f"{row[courIndex]},{courseID}" if row[courIndex] else courseID
                updated = True;
            rows.append(row);

    if not updated:
        print("Instructor not found!");     #error handing
        return;

    # Write back the data, including the header
    with open(instFile, mode='w', newline='') as file:
        writer = csv.writer(file);
        writer.writerow(headers);  # Write the header row
        writer.writerows(rows);    # Write all data rows

    print(f"Course {courseID} appended to instructor {instructorId}.");

def main():
    #Ensure the courses CSV file has the correct structure
    iniCourFile();
    
    #Load instructor IDs to validate input
    instId = loadInstIds();
    if not instId:
        print("No instructors found. Add instructors first.");      #error handing
        return;  #Exit if no instructors are available
    
    print("Adding a new course...");
    
    while True:
        instructorId = input("Enter the Instructor's ID for this course: ").strip();
        if instructorId in instId:
            print(f"Instructor ID {instructorId} is valid!");
            break;
        else:
            print("Incorrect Instructor ID. Please enter a valid ID from the instructor list.");
    
    #Prompt for course details
    #Loads previous ids for courses.
    existIds = loadExistIds();
    while True:
        courseID = input("Enter Course ID: ").strip();
        if courseID in existIds:
            print(f"Course ID is not Unique, Please try again.");
        elif " " in courseID:
            print(f"No Spaces Please");
        else:
            break;

    courseName = input("Enter Course Name: ").strip();
    instName = input("Enter Instructor's Name: ").strip();
    
    #Save the new courses to the CSV file
    with open(courFile, mode='a', newline='') as file:
        writer = csv.writer(file);
        writer.writerow([courseID, courseName, instructorId, instName]);
    
    print(f"Course {courseName} with ID {courseID} added successfully, taught by Instructor {instName}!");
    appendCourse(instructorId, courseID);

