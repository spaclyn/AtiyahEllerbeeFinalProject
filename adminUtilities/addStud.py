"""
File Name: addInst.py
Purpose:
   add instructor functionality

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import os;
import csv;

#FILE PATHS
dataFolder = "data";
studFile = os.path.join(dataFolder,"students.csv");

#Ensures the CSV file exists with the proper header.
def iniStudFile():
    if not os.path.exists(studFile):
        with open(studFile, mode='w', newline='') as file:
            writer = csv.writer(file);
            # Add headers to the CSV file
            writer.writerow(["studentID", "firstName", "lastName", "passWord"]);

#Load existing student IDs from the file.
def loadExistIds():
    existIds = set();
    try:
        with open(studFile, mode='r') as file:
            reader = csv.reader(file);
            next(reader, None);  #Skip the header row
            for row in reader:
                if row:  #Avoids processing empty rows
                    existIds.add(row[0]);

    except FileNotFoundError:
        #If the file doesn't exist, file assumes no students are present yet
        pass;
    return existIds;

#Ensure the CSV file has the correct structure
def main():
    iniStudFile();
    
    print("Adding a new student...");
    existIds = loadExistIds();

    while True:
        studId = input("Enter Student's ID: ").strip();
        if studId in existIds:
            print(f"Student ID is not Unique, Please try again.");      #error handling
        elif " " in studId:
            print(f"No Spaces Please");
        else:
            break;
    firstName = input("Enter Student's First Name: ");
    lastName = input("Enter Student's Last Name: ");
    while True:
        passWord = input("Enter Student's Password: ").strip()
        if " " not in passWord:
            break #exit loop if no whitespace
        else:
            print("Input cannot contain spaces. Try again.") 
    name = firstName + ' ' + lastName;
    
    # Save the new student to the CSV file
    with open(studFile, mode='a', newline='') as file:
        writer = csv.writer(file);
        writer.writerow([studId, firstName, lastName, passWord]);
    
    print(f"Student {name} with ID {studId} has been added successfully!");
