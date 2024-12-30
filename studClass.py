"""
File Name: studClass.py
Purpose:
   student class

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

from userClass import User;
from studUtilities import enroll, changePass;

class Student(User):
    def __init__(self, username, password):
        super().__init__(username, password);  #Call the User class constructor
    
    def viewEnroll(self):
        #Call the viewTeaching function for this student.
        enroll.viewEnrollment(self.username);  #Use self.username from User class

    def changePassword(self):
        #Provide functionality to change the password.
        changePass.changePassword(self.username);