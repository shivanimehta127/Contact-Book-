# Contact-Book

Contact Book Application 📒
This project is a Python-based Contact Book application designed to manage your personal or professional contacts efficiently. It provides a simple yet powerful way to store, update, view, and delete contact information. This application is ideal for beginners learning Python or those looking to create a basic contact management system.

Features ✨

1. Add a Contact
Easily add new contacts with the following details:
    Name: The unique identifier for each contact.
    Phone Number: A valid phone number.
    Email Address: An email address for correspondence.
If the contact already exists, the program will notify you.

2. View All Contacts
Retrieve and display the entire list of saved contacts with their details:
    Name
    Phone Number
    Email Address
If the contact book is empty, the program will inform you.

3. Update a Contact
    Modify the details of an existing contact:
    Update the phone number.
    Update the email address.
    The application ensures that only existing contacts are updated, and it provides a message if the contact does not exist.

4. Delete a Contact
    Remove a contact from the contact book by specifying their name. The application confirms deletion and notifies you if the contact is not found.


How It Works 🔧
  Data Storage: Contacts are stored in a Python dictionary, where each name acts as a unique key, and the associated value is another dictionary containing the contact's phone number and email.
  Functions:
      create_contact: Adds a new contact.
      view_contact: Displays all saved contacts.
      update_contact: Updates an existing contact's details.
      delete_contact: Deletes a contact by name.

Code Highlights 💡
Here’s an overview of the core functions:
Create Contact:
    python
    Copy code
    def create_contact(contacts, name, phone, email):
        if name in contacts:
            print(f"{name} is already present in contacts")
        else:
            contacts[name] = {"Phone": phone, "email": email}
            print(f"{name} is added.")

        
View Contact:
    python
    Copy code
    def view_contact(contacts):
        if not contacts:
            print("Contact book is empty")
        else:
            print("Contacts List")
            for name, details in contacts.items():
                print(f"Name - {name}, Phone - {details['Phone']}, email - {details['email']}")
                
Update Contact:
    python
    Copy code
    def update_contact(contacts, name, phone=None, email=None):
        if name in contacts:
            if phone:
                contacts[name]['Phone'] = phone
                print(f"Contact {name} phone number updated.")
            if email:
                contacts[name]['email'] = email
                print(f"Contact {name} email updated.")
        else:
            print("Contact not found")
            
Delete Contact:
    python
    Copy code
    def delete_contact(contacts, name):
        if name in contacts:
            del contacts[name]
            print(f"{name} is deleted")
        else:
            print("Contact not found")

            
Prerequisites
Python 3.x installed on your machine.


Run the Python script:
bash
Copy code
python contact_book.py


Usage Examples 📘
    Add a Contact: Input the name, phone number, and email address when prompted.
    View Contacts: Select the "view" option to display all saved contacts.
    Update a Contact: Specify the name of the contact you want to update and provide the new details.
    Delete a Contact: Enter the name of the contact you wish to remove.
    Potential Improvements 🛠️
    
Here are some suggestions to enhance the project:
    Add a graphical user interface (GUI) using libraries like Tkinter or PyQt.
    Save contacts to a file (e.g., CSV, JSON) for persistence across sessions.
    Add input validation to ensure phone numbers and email addresses are valid.
    Include search functionality to quickly find contacts.
    Integrate with external APIs for additional features like syncing with phone contacts.
    
License 📜
    This project is open source and available under the MIT License.
