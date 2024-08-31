class ContactManager:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email=None):
            self.contacts[name] = {'phone': phone, 'email': email}

    def update_contact(self, name, phone=None, email=None):
        if name in self.contacts:
            if phone:
                self.contacts[name]['phone'] = phone
            if email:
                self.contacts[name]['email'] = email
        else:
            print(f"Contact '{name}' not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]

        else:
            print(f"Contact '{name}' not found.")

    def list_contacts(self):
        if self.contacts:
            print("All Contacts:")
            for name, info in self.contacts.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email'] or 'N/A'}")
        else:
            print("No contacts found.")

    def search_contact(self, query):
        results = {name: info for name, info in self.contacts.items() if query.lower() in name.lower() or (info['email'] and query.lower() in info['email'].lower())}
        if results:
            print("Search Results:")
            for name, info in results.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email'] or 'N/A'}")
        else:
            print(f"No contacts found for '{query}'.")

    def list_contacts_by_initial(self, initial):
        results = {name: info for name, info in self.contacts.items() if name.lower().startswith(initial.lower())}
        if results:
            print(f"Contacts starting with '{initial}':")
            for name, info in results.items():
                print(f"Name: {name}, Phone: {info['phone']}, Email: {info['email'] or 'N/A'}")
        else:
            print(f"No contacts found starting with '{initial}'.")


def main():
    manager = ContactManager()

    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. Update Contact")
        print("3. Delete Contact")
        print("4. List All Contacts")
        print("5. Search Contacts")
        print("6. List Contacts by Initial Letter")
        print("7. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            manager.add_contact(name, phone, email)

        elif choice == '2':
            name = input("Enter name of the contact to update: ")
            phone = input("Enter new phone number (leave blank to skip): ")
            email = input("Enter new email (leave blank to skip): ")
            manager.update_contact(name, phone or None, email or None)

        elif choice == '3':
            name = input("Enter name of the contact to delete: ")
            manager.delete_contact(name)

        elif choice == '4':
            manager.list_contacts()

        elif choice == '5':
            query = input("Enter name or email to search: ")
            manager.search_contact(query)

        elif choice == '6':
            initial = input("Enter the initial letter: ")
            manager.list_contacts_by_initial(initial)

        elif choice == '7':
            print("Exiting Contact Management System.")
            break

        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main()




