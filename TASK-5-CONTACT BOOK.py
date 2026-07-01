#CONTACT BOOK WHICH CAN VIEW, ADD, DELETE AND SEARCH CONTACT
# Initialize an empty dictionary to store contacts
# Structure: { "Name": "Phone Number" }
contacts = {}

def display_menu():
    print("\n--- CONTACT LIST MANAGER ---")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Update Contact")
    print("4. Delete Contact")
    print("5. Search Contact")
    print("6. Exit")

while True:
    display_menu()
    choice = input("Enter your choice (1-6): ")

    # Feature 1: Adding a new contact
    if choice == '1':
        name = input("Enter contact name: ").strip()
        phone = input("Enter phone number: ").strip()
        contacts[name] = phone
        print(f"Contact '{name}' added successfully!")

    # Feature 2: Viewing all contacts
    elif choice == '2':
        if not contacts:
            print("Your contact list is empty.")
        else:
            print("\n--- ALL CONTACTS ---")
            for name, phone in contacts.items():
                print(f"Name: {name} | Phone: {phone}")

    # Feature 3: Updating an existing contact
    elif choice == '3':
        name = input("Enter the name of the contact to update: ").strip()
        if name in contacts:
            new_phone = input(f"Enter new phone number for {name}: ").strip()
            contacts[name] = new_phone
            print("Contact updated successfully!")
        else:
            print("Contact not found.")

    # Feature 4: Deleting a contact
    elif choice == '4':
        name = input("Enter the name to delete: ").strip()
        if name in contacts:
            del contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")

    # Feature 5: Searching for a specific contact
    elif choice == '5':
        name = input("Enter name to search: ").strip()
        # .get() returns the value if it exists, otherwise it returns None
        phone = contacts.get(name)
        if phone:
            print(f"Found: {name} - {phone}")
        else:
            print("Contact not found.")

    # Feature 6: Exit the program
    elif choice == '6':
        print("Exiting program. Goodbye!")
        break

    else:
        print("Invalid choice, please try again.")

