"""
File Name: adminClass.py
Purpose:
   admin class

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

from userClass import User;
from adminUtilities import addCour; 
from adminUtilities import addInst;
from adminUtilities import addStud;
from adminUtilities import viewMenu;
from adminUtilities import viewEnroll;

class Admin(User):
    def __init__(self, username, password):
        super().__init__(username, password);

    def addStudent(self):
        print("Loading Students...");
        try:
            addStud.main();  #Call addStud functionality
        except AttributeError:      #error handling
            print("Error: Unable to call addStud.main().");
        except Exception as e:
            print(f"An error occurred while adding students: {e}");

    def addCourse(self):
        print("Loading courses....");
        try:
            addCour.main();  #Call addCour functionality.
        except AttributeError:      #error handling
            print("Error: Unable to call addCour.main().");
        except Exception as e:
            print(f"An error occurred while adding a course: {e}");

    def addInstructor(self):
        print("Loading Instructors...");
        try:
            addInst.main();  #Call addInst functionality
        except AttributeError:      #error handling
            print("Error: Unable to call addInst.main().");
        except Exception as e:
            print(f"An error occurred while adding an instructor: {e}");

    def viewCourse(self):
        print("Loading Courses...");
        try:
            viewMenu.main();  #Call View Courses functionality
        except AttributeError:      #error handling
            print("Error: Unable to call viewMenu.py.");
        except Exception as e:
            print(f"An error occurred while viewing courses: {e}");

    def viewInstructors(self):
        print("Loading Courses...");
        try:
            viewMenu.inst();  #Call View Inst functionality
        except AttributeError:      #error handling
            print("Error: Unable to call viewMenu.py.");
        except Exception as e:
            print(f"An error occurred when viewing instructors: {e}"); 

    def viewStudents(self):
        print("Loading Students...")
        try:
            viewMenu.stud();  #Call View Students functionality
        except AttributeError:      #error handling
            print("Error: Unable to call viewMenu.py.");
        except Exception as e:
            print(f"An error occurred when viewing students: {e}"); 

    def viewEnrollment(self):
        print("Loading Enrollments...");
        try:
            viewEnroll.viewAllEnrollments(); #ViewEnroll Functionality.
        except AttributeError:      #error handling
            print("Error: Unable to call viewEnroll.py.");
        except Exception as e:
            print(f"An error ouccured when viewing enrollments: {e}");
