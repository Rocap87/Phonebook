#Function to add phone number
def add_phone_number(dictionary, name, phone):
    """Add names and phone numbers to phone book"""
    dictionary[name] = phone
    #Confirm addition of new name and number to the dictionary
    return "Contact added"


#Function to remove phone number    
def remove_phone_number(dictionary, name_to_delete):
    """Ask user which contact to delete from phone book"""
    if name_to_delete in dictionary:
        dictionary.pop(name_to_delete)
        #Confirm the contact has been deleted
        return "Contact deleted"
    else:
        #Warn that contact to be delete is not in the phone book
        return "Contact not present in phone book"
    

#Function to search for contact numbers
def search_for_name(dictionary, name_to_search):
    """Ask user which contact's phone number to look up"""
    #Message to display if name is not in the phone book
    message = "Name not found"
    for name in dictionary:
        if name == name_to_search:
            #Message to display if the name is in the phone book
            message = name_to_search + "  " + dictionary[name_to_search]
    #Return the appropriate message
    return(message)

#Function to display phone book menu
def print_menu():
    """Ask user which action to perform"""
    #The variable menu will prompt the menu of the application to be displayed.
    #By inserting a value between 1 and 5 the user will perform 
    #one of the below actions.
    menu = input("""Menu
   
    1) Add a Phone Number
    2) Remove a Phone Number
    3) Search for a Phone Number
    4) Print Phone Book
    5) Quit
    What do you want to do in the phone book? Enter 5 to finish the program:""")
    return menu

#Function that runs the program    
def user_interface():
    """Based on input of print_menu() the user access the required function"""
    while True:
        menu = print_menu()
        #After the function print_menu() is run, the user can quit the 
        #program by inputting "5"
        if menu == "5":
            break
        elif menu == "1":
            #Ask for the name and number to add to the phone book. 
            name = input("Name: ").capitalize()
            phone = input("Number: ")
            #Run the function add_phone_number() and add the inputs to a
            #dictionary called contacts
            print(add_phone_number(contacts, name, phone))
        elif menu == "2":
            #Ask user which contacts to delete from phone book
            contact_to_delete = input("Name to delete: ").capitalize()
            #Run the function remove_phone number and remove the provided  
            #name and associated phone number from dictionary contacts
            print(remove_phone_number(contacts, contact_to_delete))
        elif menu == "3":
            #Ask user for the name to lookup in the dictionary to retrieve 
            #the associated phone number
            search_user  = input("Name to search:").capitalize()
            #Search in the contacts for the name inserted by the user and 
            #print it with its associated phone number
            print(search_for_name(contacts, search_user))
        elif menu == "4":
            #If the dictionary contacts is empty the application confirms 
            #the phone book is empty
            if len(contacts) == 0:
                print("Phone book empty. Add some contacts")
            #If there are entries in the phone book
            else:
                #Ask user in which alpabetical order to display the phone book
                order_choice = input("For phone book ordered A-Z press 1. For phone book ordered Z-A press 2: ") 
                #If user inserts 1 the phone book is displayed A to Z
                if order_choice == "1":
                    for name in sorted(contacts):
                        print(name, contacts[name])
                #If user inserts 2 the phone book is displayed Z to A
                elif order_choice == "2":
                    for name in sorted(contacts, reverse = True):
                        print(name, contacts[name])
                #If user inserts a value different from 1 or 2 print warning message
                else:
                    print("Wrong command!")
        #If user insert a value different from 1 to 5 following the prompt of 
        #print_menu, print a warning message
        else:
            print("Try again")

#Dictionary for storing names and phone numbers
contacts = {}
#Run the application 
user_interface()

"""=============================CODE END==================================="""

"""=============================TEST CASES================================="""
print("Begin of test cases")

"""TEST 1"""        
"""The user will run the code below. If a value different from 1-5 is inserted
the function will return a "Try again" message and prompt the menu options again.
If the user inserts the number 5 the while loop ends and the users quits the program."""

print("Test 1")

def print_menu():
    """Ask user which action to perform"""
    menu = input("""Menu
   
    1) Add a Phone Number
    2) Remove a Phone Number
    3) Search for a Phone Number
    4) Print Phone Book
    5) Quit
    What do you want to do in the phone book? Enter 5 to finish the program:""")
    return menu

def user_interface():
    """Based on input of print_menu() the user access the required function"""
    while True:
        menu = print_menu()
        if menu == "5":
            break
        elif menu == "1":
            name = input("Name: ").capitalize()
            phone = input("Number: ")
            print(add_phone_number(contacts, name, phone))
        elif menu == "2":
            contact_to_delete = input("name to delete: ").capitalize()
            print(remove_phone_number(contacts, contact_to_delete))
        elif menu == "3":
            search_user  = input("Name to search:").capitalize()
            print(search_for_name(contacts, search_user))
        elif menu == "4":
            if len(contacts) == 0:
                print("Phone book empty. Add some contacts")
            else:
                order_choice = input("For phone book ordered A-Z press 1. For phone book ordered Z-A press 2: ") 
                if order_choice == "1":
                    for name in sorted(contacts):
                        print(name, contacts[name])
                elif order_choice == "2":
                    for name in sorted(contacts, reverse = True):
                        print(name, contacts[name])
                else:
                    print("Wrong command!")
        else:
            print("Try again")
contacts= {"Mark":"11111", "Samuel":"89745", "Mike":"9475", "John":"555867", "Sandra":"5687"}
user_interface()

"""TEST 2"""
"""The user will run the code below, input "1" to add a phone number 
and two prompts will be displayed: the first prompt asks to insert a name 
and the second asks to insert a phone number. The function will add both 
to the dictionary "contacts" and returns a message "Contact added".
Repeat the action for 5 times and then input "4" to print the phone book
and choose in which order to display it. The outcome will be a phone book
comprehensive of the pre-populated entries with addition of the new
contacts added by the user. Quit the program (input "5") and the phone book is
printed to the console to verify that the new contacts have been added to the 
dictionary."""

print("Test 2")

def add_phone_number(dictionary, name, phone):
    """Add names and phone numbers to phone book"""
    dictionary[name] = phone
    return "Contact added"

def print_menu():
    """Ask user which action to perform"""
    menu = input("""Menu
   
    1) Add a Phone Number
    2) Remove a Phone Number
    3) Search for a Phone Number
    4) Print Phone Book
    5) Quit
    What do you want to do in the phone book? Enter 5 to finish the program:""")
    return menu

def user_interface():
    """Based on input of print_menu() the user access the required function"""
    while True:
        menu = print_menu()
        if menu == "5":
            break
        elif menu == "1":
            name = input("Name: ").capitalize()
            phone = input("Number: ")
            print(add_phone_number(contacts, name, phone))
        elif menu == "2":
            contact_to_delete = input("Name to delete: ").capitalize()
            print(remove_phone_number(contacts, contact_to_delete))
        elif menu == "3":
            search_user  = input("Name to search:").capitalize()
            print(search_for_name(contacts, search_user))
        elif menu == "4":
            if len(contacts) == 0:
                print("Phone book empty. Add some contacts")
            else:
                order_choice = input("For phone book ordered A-Z press 1. For phone book ordered Z-A press 2: ") 
                if order_choice == "1":
                    for name in sorted(contacts):
                        print(name, contacts[name])
                elif order_choice == "2":
                    for name in sorted(contacts, reverse = True):
                        print(name, contacts[name])
                else:
                    print("Wrong command!")
        else:
            print("Try again")
contacts= {"Mark":"11111", "Samuel":"89745", "Mike":"9475", "John":"555867", "Sandra":"5687"}
user_interface()
#when printing contacts after adding 5 new contacts and quitting the application the user should see the 5 contacts included in the pre-populated dictionary
print(contacts)

"""TEST 3"""
"""The user will run the code below and input "2" to remove a phone number.
The application will ask for the name to be deleted from contacts. Enter
the name "Charles", which is not in contacts. The application returns the 
message "Contact not present in the phone book". Input "2" again 
and now input "Mike". The application will return: "Contact deleted."
Input "4" to print the phone book and choose in which order to display it. 
The outcome will be a phone book comprehensive of the pre-populated 
entries apart for Mike and his number.
Input "5" to quit. The phone book is printed to the console to confirm that
the entry for Mike and the associated phone number is no longer present in 
the dictionary."""

print("Test 3")

def remove_phone_number(dictionary, name_to_delete):
    """Ask user which contact to delete from phone book"""
    if name_to_delete in dictionary:
        dictionary.pop(name_to_delete)
        return "Contact deleted"
    else:
        return "Contact not present in phone book"

def print_menu():
    """Ask user which action to perform"""
    menu = input("""Menu
   
    1) Add a Phone Number
    2) Remove a Phone Number
    3) Search for a Phone Number
    4) Print Phone Book
    5) Quit
    What do you want to do in the phone book? Enter 5 to finish the program:""")
    return menu
    
def user_interface():
    """Based on input of print_menu() the user access the required function"""
    while True:
        menu = print_menu()
        if menu == "5":
            break
        elif menu == "1":
            name = input("Name: ").capitalize()
            phone = input("Number: ")
            print(add_phone_number(contacts, name, phone))
        elif menu == "2":
            contact_to_delete = input("Name to delete: ").capitalize()
            print(remove_phone_number(contacts, contact_to_delete))
        elif menu == "3":
            search_user  = input("Name to search:").capitalize()
            print(search_for_name(contacts, search_user))
        elif menu == "4":
            if len(contacts) == 0:
                print("Phone book empty. Add some contacts")
            else:
                order_choice = input("For phone book ordered A-Z press 1. For phone book ordered Z-A press 2: ") 
                if order_choice == "1":
                    for name in sorted(contacts):
                        print(name, contacts[name])
                elif order_choice == "2":
                    for name in sorted(contacts, reverse = True):
                        print(name, contacts[name])
                else:
                    print("Wrong command!")
        else:
            print("Try again")

contacts= {"Mark":"11111", "Samuel":"89745", "Mike":"9475", "John":"555867", "Sandra":"5687"}
user_interface()
print(contacts)

"""TEST 4"""
"""Run the code below and input "3" to search for a phone number. 
The application searches for the name to retrieve from the dictionary. 
If the user enters the name "Charles", the application will return the message 
"Name not found". Input "3" again and input the name "Mike". The application returns
the name searched for and the associated phone number. Input "5" to quit."""

print("Test 4")

def search_for_name(dictionary, name_to_search):
    """Ask user which contact's phone number to look up"""
    message = "Name not found"
    for name in dictionary:
        if name == name_to_search:
            message = name_to_search + "  " + dictionary[name_to_search]
    return(message)

def print_menu():
    """Ask user which action to perform"""
    menu = input("""Menu
   
    1) Add a Phone Number
    2) Remove a Phone Number
    3) Search for a Phone Number
    4) Print Phone Book
    5) Quit
    What do you want to do in the phone book? Enter 5 to finish the program:""")
    return menu
    
def user_interface():
    """Based on input of print_menu() the user access the required function"""
    while True:
        menu = print_menu()
        if menu == "5":
            break
        elif menu == "1":
            name = input("Name: ").capitalize()
            phone = input("Number: ")
            print(add_phone_number(contacts, name, phone))
        elif menu == "2":
            contact_to_delete = input("Name to delete: ").capitalize()
            print(remove_phone_number(contacts, contact_to_delete))
        elif menu == "3":
            search_user  = input("Name to search:").capitalize()
            print(search_for_name(contacts, search_user))
        elif menu == "4":
            if len(contacts) == 0:
                print("Phone book empty. Add some contacts")
            else:
                order_choice = input("For phone book ordered A-Z enter 1. For phone book ordered Z-A enter 2: ") 
                if order_choice == "1":
                    for name in sorted(contacts):
                        print(name, contacts[name])
                elif order_choice == "2":
                    for name in sorted(contacts, reverse = True):
                        print(name, contacts[name])
                else:
                    print("Wrong command!")
        else:
            print("Try again")

contacts= {"Mark":"11111", "Samuel":"89745", "Mike":"9475", "John":"555867", "Sandra":"5687"}
user_interface()


"""TEST 5"""
"""Run the code below and input "4" to display the phone book.
An if statement checks the length of the dictionary contacts
to establish if there are any entries. If the length equals to 0
it means there are no contacts in the dictionary and a message will be 
displayed: "Phone book empty. Add some contacts". Input "5" to quit."""

print("Test 5")

def print_menu():
    """Ask user which action to perform"""
    menu = input("""Menu
   
    1) Add a Phone Number
    2) Remove a Phone Number
    3) Search for a Phone Number
    4) Print Phone Book
    5) Quit
    What do you want to do in the phone book? Enter 5 to finish the program:""")
    return menu

def user_interface():
    """Based on input of print_menu() the user access the required function"""
    while True:
        menu = print_menu()
        if menu == "5":
            break
        elif menu == "1":
            name = input("Name: ").capitalize()
            phone = input("Number: ")
            print(add_phone_number(contacts, name, phone))
        elif menu == "2":
            contact_to_delete = input("Name to delete: ").capitalize()
            print(remove_phone_number(contacts, contact_to_delete))
        elif menu == "3":
            search_user  = input("Name to search:").capitalize()
            print(search_for_name(contacts, search_user))
        elif menu == "4":
            if len(contacts) == 0:
                print("Phone book empty. Add some contacts")
            else:
                order_choice = input("For phone book ordered A-Z press 1. For phone book ordered Z-A press 2: ") 
                if order_choice == "1":
                    for name in sorted(contacts):
                        print(name, contacts[name])
                elif order_choice == "2":
                    for name in sorted(contacts, reverse = True):
                        print(name, contacts[name])
                else:
                    print("Wrong command!")
        else:
            print("Try again")

contacts= {}
user_interface()

"""TEST 6"""
"""Run the code below and input "4" to display the phone book.
An if statement checks the length of the dictionary contacts
to establish if there are any entries. If the length is not 0,
a prompt asks whether to have the phone book displayed ordered from A-Z
by inserting "1", or Z-A by inserting "2".
In case is inserted a value is different from 1 or 2 a message 
"Wrong command!" is displayed. Test the 3 different scenarios and then quit
by inputting "5"."""

print("Test 6")

def print_menu():
    """Ask user which action to perform"""
    menu = input("""Menu
   
    1) Add a Phone Number
    2) Remove a Phone Number
    3) Search for a Phone Number
    4) Print Phone Book
    5) Quit
    What do you want to do in the phone book? Enter 5 to finish the program:""")
    return menu

def user_interface():
    """Based on input of print_menu() the user access the required function"""
    while True:
        menu = print_menu()
        if menu == "5":
            break
        elif menu == "1":
            name = input("Name: ").capitalize()
            phone = input("Number: ")
            print(add_phone_number(contacts, name, phone))
        elif menu == "2":
            contact_to_delete = input("Name to delete: ").capitalize()
            print(remove_phone_number(contacts, contact_to_delete))
        elif menu == "3":
            search_user  = input("Name to search:").capitalize()
            print(search_for_name(contacts, search_user))
        elif menu == "4":
            if len(contacts) == 0:
                print("Phone book empty. Add some contacts")
            else:
                order_choice = input("For phone book ordered A-Z press 1. For phone book ordered Z-A press 2: ") 
                if order_choice == "1":
                    for name in sorted(contacts):
                        print(name, contacts[name])
                elif order_choice == "2":
                    for name in sorted(contacts, reverse = True):
                        print(name, contacts[name])
                else:
                    print("Wrong command!")
        else:
            print("Try again")

contacts= {"Mark":"11111", "Samuel":"89745", "Mike":"9475", "John":"555867", "Sandra":"5687"}
user_interface()