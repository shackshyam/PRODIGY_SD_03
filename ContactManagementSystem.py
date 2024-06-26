import json

CONTACTS_FILE = 'contacts.json'


def load_contacts():
    try:
        with open(CONTACTS_FILE, 'r') as file:
            contacts = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        contacts = []
    return contacts


def save_contacts(contacts):
    with open(CONTACTS_FILE, 'w') as file:
        json.dump(contacts, file, indent=4)


def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    contacts.append({'name': name, 'phone': phone, 'email': email})
    save_contacts(contacts)
    print("Contact added successfully!")


def view_contacts(contacts):
    if contacts:
        for index, contact in enumerate(contacts):
            print(f"{index + 1}. Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
    else:
        print("No contacts found.")


def edit_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to edit: ")) - 1
        if 0 <= index < len(contacts):
            contacts[index]['name'] = input("Enter new name: ")
            contacts[index]['phone'] = input("Enter new phone number: ")
            contacts[index]['email'] = input("Enter new email address: ")
            save_contacts(contacts)
            print("Contact updated successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def delete_contact(contacts):
    view_contacts(contacts)
    try:
        index = int(input("Enter the contact number to delete: ")) - 1
        if 0 <= index < len(contacts):
            contacts.pop(index)
            save_contacts(contacts)
            print("Contact deleted successfully!")
        else:
            print("Invalid contact number.")
    except ValueError:
        print("Invalid input. Please enter a valid number.")


def main():
    contacts = load_contacts()
    while True:
        print("\nContact Manager")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Edit Contact")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact(contacts)
        elif choice == '2':
            view_contacts(contacts)
        elif choice == '3':
            edit_contact(contacts)
        elif choice == '4':
            delete_contact(contacts)
        elif choice == '5':
            print("Exiting program.")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()
