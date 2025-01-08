def create_contact(contacts,name,phone,email):
    if name in contacts:
        print(f"{name} is already present in contacts")
    else:
        contacts[name]={"Phone" : phone,"email": email}
        print(f"{name} is added.")


def view_contact(contacts):
    if not contacts:
        print("Contact book is empty")
    else:
        print("Contacts List")
        for name,details in contacts.items():
            print(f"Name - {name}, Phone - {details['Phone']},email - {details['email']}")


def update_contact(contacts, name, phone = None, email = None):
    if name in contacts:
        if phone != None:
            contacts[name]['Phone']= phone
            print(f"Contact {name} phone number updated.")
        if email !=None:
            contacts[name]['email']= email
            print(f"Contact{name} email updated.")
        else:
            print("Contact Not found")


def delete_contact(contacts,name):
    if name in contacts:
        del contacts[name]
        print(f"{name} is deleted")
    else:
        print("Contact not found")