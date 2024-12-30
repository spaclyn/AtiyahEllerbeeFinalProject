"""
File Name: mainLanding.py
Purpose:
   mainLanding is the main landing page

First Create Date: November  25, 2024
Last Update Date: 12/10, 2024
Author: Atiyah 'AJ' Ellerbee
Version: 3.10
"""

import studUtil;
import adminUtil;
import instUtil;

#LANDING PAGE
def main():
    print("\nWelcome to the Landing Menu!");

    while True:
        print("\nPlease Choose one:");

        print("1. Administrator");
        print("2. Instructor");
        print("3. Student");
        print("4. Exit");

        choice = input("Enter your choice (1-4): ").strip();

        if choice == '1':
            adminUtil.main();  #Call choice method
        elif choice == '2':
            instUtil.main();  #Call choice method
        elif choice == '3':
            studUtil.main();  #Call choice method
    
        elif choice == '4':
            print("Exiting. Bye Bye!");
            break
        else:
            print("Invalid choice. Please try again.");

if __name__ == "__main__":
    main();