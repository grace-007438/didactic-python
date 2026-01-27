import os

FILE_NAME = "contacts.txt"

# Load contacts from file
def load_contacts():
    contacts = {}
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            for line in file:
                name, phone, email = line.strip().split(",")
                contacts[name] = {"phone": phone, "email": email}
    return contacts

# Save contacts to file
def save_contacts(contacts):
    with open(FILE_NAME, "w") as file:
        for name, data in contacts.items():
            file.write(f"{name},{data['phone']},{data['email']}\n")

# Add contact
def add_contact():
    contacts = load_contacts()
    name = input("Enter name: ")

    if name in contacts:
        print("Contact already exists!")
        return

    phone = input("Enter phone: ")
    email = input("Enter email: ")

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact added successfully!")

# View contacts
def view_contacts():
    contacts = load_contacts()
    if not contacts:
        print("No contacts found.")
        return

    for name, data in contacts.items():
        print(f"Name: {name}, Phone: {data['phone']}, Email: {data['email']}")

# Search contact
def search_contact():
    contacts = load_contacts()
    name = input("Enter name to search: ")

    if name in contacts:
        print(f"Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}")
    else:
        print("Contact not found.")

# Update contact
def update_contact():
    contacts = load_contacts()
    name = input("Enter name to update: ")

    if name not in contacts:
        print("Contact not found.")
        return

    phone = input("Enter new phone: ")
    email = input("Enter new email: ")

    contacts[name] = {"phone": phone, "email": email}
    save_contacts(contacts)
    print("Contact updated successfully!")

# Delete contact
def delete_contact():
    contacts = load_contacts()
    name = input("Enter name to delete: ")

    if name in contacts:
        del contacts[name]
        save_contacts(contacts)
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

# Main menu
def main():
    while True:
        print("\n--- Contact Management System ---")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            add_contact()
        elif choice == "2":
            view_contacts()
        elif choice == "3":
            search_contact()
        elif choice == "4":
            update_contact()
        elif choice == "5":
            delete_contact()
        elif choice == "6":
            print("Thank you! Exiting...")
            break
        else:
            print("Invalid choice!")

main()
