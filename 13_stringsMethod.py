import pickle
import os

FILENAME = "phonebook.dat"

# -------------------------------
# Helper Functions
# -------------------------------

def load_contacts():
    if not os.path.exists(FILENAME):
        return []
    with open(FILENAME, "rb") as f:
        return pickle.load(f)

def save_contacts(contacts):
    with open(FILENAME, "wb") as f:
        pickle.dump(contacts, f)

def menu_design(title):
    print("\n" + "=" * 30)
    print(title)
    print("=" * 30)

# -------------------------------
# Core Functions
# -------------------------------

def add_contact():
    contacts = load_contacts()

    while True:
        menu_design("ADD NEW CONTACT")

        name = input("Enter Name: ")
        address = input("Enter Address: ")
        email = input("Enter Email: ")
        phone = input("Enter Phone Number: ")

        contact = {
            "name": name,
            "address": address,
            "email": email,
            "phone": phone
        }

        contacts.append(contact)
        save_contacts(contacts)

        print("\nContact Added Successfully!")

        choice = input("Add another? (y/n): ").lower()
        if choice != 'y':
            break


def view_contacts():
    contacts = load_contacts()
    menu_design("ALL CONTACTS")

    if not contacts:
        print("No contacts found.")
        return

    for c in contacts:
        print(f"\nName: {c['name']}")
        print(f"Address: {c['address']}")
        print(f"Email: {c['email']}")
        print(f"Phone: {c['phone']}")


def search_contact():
    contacts = load_contacts()
    menu_design("SEARCH CONTACT")

    keyword = input("Enter name to search: ").lower()
    found = 0

    for c in contacts:
        if keyword in c["name"].lower():
            print(f"\nName: {c['name']}")
            print(f"Address: {c['address']}")
            print(f"Email: {c['email']}")
            print(f"Phone: {c['phone']}")
            found += 1

    if found == 0:
        print("No matching contact found.")
    else:
        print(f"\nTotal {found} contact(s) found.")


def delete_contact():
    contacts = load_contacts()
    menu_design("DELETE CONTACT")

    name = input("Enter name to delete: ").lower()
    new_contacts = [c for c in contacts if c["name"].lower() != name]

    if len(new_contacts) == len(contacts):
        print("No contact found.")
    else:
        save_contacts(new_contacts)
        print("Contact deleted successfully!")


def modify_contact():
    contacts = load_contacts()
    menu_design("MODIFY CONTACT")

    name = input("Enter name to modify: ").lower()

    for c in contacts:
        if c["name"].lower() == name:
            print("Enter new details:")
            c["name"] = input("New Name: ")
            c["address"] = input("New Address: ")
            c["email"] = input("New Email: ")
            c["phone"] = input("New Phone: ")

            save_contacts(contacts)
            print("Contact modified successfully!")
            return

    print("No contact found.")


# -------------------------------
# Main Menu
# -------------------------------

def main_menu():
    while True:
        menu_design("PHONEBOOK MANAGEMENT SYSTEM")

        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Modify Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            modify_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            print("Exiting...")
            break
        else:
            print("Invalid choice! Try again.")


# Run Program
if __name__ == "__main__":
    main_menu()