# Phonebook
Application for PGCert Computer Science University of Essex (Launching into Computer Science).

This application is a phone book which enables the user to add new contacts, delete and search for a contact, and display the phone book.
The application displays prompt messages before performing an action.

# Instructions
The code is written in Python and can be run in the workspace available on Codio. The user needs to open the file phonebook.py to have access to the code.
The code consists of a series of functions to enable the user to perform the operations offered by the application. When the user runs the entire code, a user interface is displayed and the user is prompted to choose which action to perform.
Central to the code is the user_interface() function, which is based on a while loop breaking when the user inserts the value corresponding to the action “Quit”.
The application starts with an empty dictionary called “contacts” in which all names and numbers are stored.
The user_interface() function has the following actions to choose from: 1. Addaphonenumber:
The action accesses the function add_phone_number(dictionary, name, phone) to add a name and phone number to the dictionary “contacts”. The application will prompt a message requesting to insert a name and phone
6
number. The name will be automatically capitalized when stored.
2. Removeaphonenumber:
The action accesses the function remove_phone_number(dictionary, name_to_delete) which removes the name provided by the user as well as the corresponding number saved in the phone book.
3. Searchforaphonenumber:
The action accesses the function search_for_name(dictionary, name_to_search) which searches for the name provided when prompted “Name to search:”. If found, the name and the associated phone number are displayed.
4. Printthephonebook:
The action initiates an if-statement that checks the length of the phonebook to verify whether it is empty. If it is not empty, a prompt asks whether to display the phone book in ascending or descending alphabetical order.
5. Quittheprogram:
The action breaks the while loop of user_interface() and the application stops.
