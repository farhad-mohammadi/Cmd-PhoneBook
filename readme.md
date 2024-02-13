Phonebook
This project is a simple command line phonebook application that demonstrates object oriented programming in Python. It allows you to create, save, edit, delete, and search contacts using a text-based interface.

Installation
To run this project, you need to have Python 3 installed on your system. You can download it from https://www.python.org/downloads/.

You also need to have the pickle and prompt_toolkit modules, which are libraries for Python. You can check if you have them by running:

import pickle
import prompt_toolkit

If you don't get any error, you have the modules installed.

If you don't have the prompt_toolkit module, you can install it by running:

pip install prompt_toolkit

Usage
To use this project, you need to have two files in the same directory: phonebook.py and cmd_phonebook.py.

The phonebook.py file contains two classes: Contact and Phonebook. The Contact class represents a contact with various attributes, such as name, phone, email, etc. The Phonebook class represents a phonebook with a list of contacts, and methods for adding, saving, deleting, editing, finding, and sorting contacts.

The cmd_phonebook.py file contains a program that uses the classes from phonebook.py to create a command line phonebook. It has a menu with different options, such as:

•  Add a new contact

•  Save contacts

•  Delete a contact

•  Edit a contact

•  Find a contact

•  Exit

To run the program, you need to open a terminal or a command prompt, and navigate to the directory where the files are located. Then, you need to run the following command:

python cmd_phonebook.py

This will start the program and show you the menu. You can choose an option by entering the corresponding number. For example, if you want to add a new contact, you can enter 1. Then, you will be asked to enter the details of the contact, such as first name, last name, phone, etc. You can leave any field blank if you don't want to fill it. After you enter the details, the contact will be added to the phonebook.

You can repeat this process for other options, such as saving, deleting, editing and finding contacts. To exit the program, you can choose option 4.

Examples
Here are some examples of how the program works:

Welcome to the phonebook!
[1] Select 
[2] Find
[3] New
[4] Exit
Please enter the number of one of the options:

1
Enter the first name: Alice
Enter the last name: Smith
Enter the phone: 1234567890
Enter the home phone: 
Enter the work phone: 
Enter the job: 
Enter the address: 
Enter the email: alice@gmail.com
Enter the facebook ID: 
Enter the telegram ID: 
Enter the instagram ID: 
Contact added successfully!