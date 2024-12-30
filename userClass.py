"""
File Name: userClass.py
Purpose:
   user parent class

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

class User:
    def __init__(self, username, password):
        self.username = username;  #attribute assignment
        self.password = password;

    def authenticate(self, inputPass):
        return self.password == inputPass;
