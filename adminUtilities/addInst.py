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
instFile = os.path.join(dataFolder,"instructors.csv");

#Ensures the CSV file exists with the proper header.
def iniInstFile():
    if not os.path.exists(instFile):
        with open(instFile, mode='w', newline='') as file:
            writer = csv.writer(file);
            #Add headers to the CSV file
            writer.writerow(["instID","instTitle", "firstName", "lastName", "passWord","courses"]);

#Load existing Instructor IDs from the file.
def loadExistIds():
    existIds = set();
    try:
        with open(instFile, mode='r') as file:
            reader = csv.reader(file);
            next(reader, None)  #Skips the header row
            for row in reader:
                if row:  #Avoid processing empty rows
                    existIds.add(row[0]); 
    
    except FileNotFoundError:
        #If the file doesn't exist, file assumes instructors are present yet
        pass;
    return existIds;

def main():
    #Makes sure that CSV file has header
    iniInstFile();

    print("Adding a new Instructor...");
    existIds = loadExistIds();

    while True:
        instId = input("Enter Instructor's ID: ").strip();
        if instId in existIds:
            print(f"Instructor Id: {instId} already exists. Please try a unique input.");       #error handing
        elif " " in instId:
            print(f"No Spaces Please");
        else:
            break; 
    instTitle = input("Enter The Instuctor's Title (If n/a, please hit enter): ");
    firstName = input("Enter Instructor's First Name: ");
    lastName = input("Enter Instructor's Last Name: ");
    while True:
        passWord = input("Enter Instructor's Password: ").strip()
        if " " not in passWord:
            break #exit loop if no whitespace
        else:
            print("Input cannot contain spaces. Try again.") 
    name = instTitle + ' ' +firstName + ' ' + lastName;
    
    #Saves The Information to the CSV.
    with open(instFile, mode='a', newline='') as file:
        writer = csv.writer(file);
        writer.writerow([instId, instTitle, firstName, lastName, passWord, ""]);
    
    print(f"Instructor {name} with ID: {instId} added successfully!");
