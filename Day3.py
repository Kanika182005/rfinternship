# Phonebook Dictionary
phonebook = {
    "Amit": "9876543210",
    "Riya": "9123456780"
}

# Function to add contact
def add_contact():
    name = input("Enter name: ").title()
    
    # Prevent duplicate entries
    if name in phonebook:
        print("Contact already exists!")
    else:
        number = input("Enter phone number: ")
        phonebook[name] = number
        print("Contact added successfully!")

# Function to search contact
def search_contact():
    name = input("Enter name to search: ").title()
    
    # Exact search
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        # Partial search bonus
        found = False
        for contact in phonebook:
            if name.lower() in contact.lower():
                print(f"{contact}: {phonebook[contact]}")
                found = True
        
        if not found:
            print("Contact not found!")

# Function to delete contact
def delete_contact():
    name = input("Enter name to delete: ").title()
    
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found!")

# Function to display all contacts
def show_contacts():
    if len(phonebook) == 0:
        print("Phonebook is empty!")
    else:
        print("\nAll Contacts:")
        for name, number in phonebook.items():
            print(f"{name}: {number}")

# Main Menu
while True:
    print("\n===== PHONEBOOK MENU =====")
    print("1. Add Contact")
    print("2. Search Contact")
    print("3. Delete Contact")
    print("4. Show All Contacts")
    print("5. Exit")
    
    choice = input("Enter your choice: ")
    
    if choice == "1":
        add_contact()
    elif choice == "2":
        search_contact()
    elif choice == "3":
        delete_contact()
    elif choice == "4":
        show_contacts()
    elif choice == "5":
        print("Exiting Phonebook...")
        break
    else:
        print("Invalid choice! Try again.")