"""
File Name: instrClass.py
Purpose:
   instructor class

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

from userClass import User;
from instrUtilities.viewTeaching import viewTeaching;

class Instructor(User):
    def __init__(self, username, password):
        super().__init__(username, password);  # Call the User class constructor

    def viewCourses(self):
        #Call the viewTeaching function for this instructor.
        viewTeaching(self.username);  # Use self.username from User class