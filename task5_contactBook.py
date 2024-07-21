# Note : This program holds contacts temporarily.
# This program does not store contacts persistently. 
# Once we exit the program, all contacts will be lost. 
# To store contacts persistently, 
# Modify the program to use a database or file storage.

class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self):
        name = input("Enter name: ")
        phone = input("Enter phone number: ")
        email = input("Enter email: ")
        self.contacts[name] = {"phone": phone, "email": email}
        print("Contact added successfully!")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts available!")
        else:
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email']}")

    def search_contact(self):
        name = input("Enter name to search: ")
        if name in self.contacts:
            print(f"Name: {name}, Phone: {self.contacts[name]['phone']}, Email: {self.contacts[name]['email']}")
        else:
            print("Contact not found!")

    def update_contact(self):
        name = input("Enter name to update: ")
        if name in self.contacts:
            phone = input("Enter new phone number: ")
            email = input("Enter new email: ")
            self.contacts[name] = {"phone": phone, "email": email}
            print("Contact updated successfully!")
        else:
            print("Contact not found!")

    def delete_contact(self):
        name = input("Enter name to delete: ")
        if name in self.contacts:
            del self.contacts[name]
            print("Contact deleted successfully!")
        else:
            print("Contact not found!")

contact_book = ContactBook()
while True:
    print("\n1. Add contact")
    print("2. View contacts")
    print("3. Search contact")
    print("4. Update contact")
    print("5. Delete contact")
    print("6. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        contact_book.add_contact()
    elif choice == "2":
        contact_book.view_contacts()
    elif choice == "3":
        contact_book.search_contact()
    elif choice == "4":
        contact_book.update_contact()
    elif choice == "5":
        contact_book.delete_contact()
    elif choice == "6":
        print("Thank you for using Contact Book")
        break
    else:
        print("Invalid choice. Please try again.")
