class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self):
        name = input("Enter name: ")
        phone_number = input("Enter phone number: ")
        email = input("Enter email: ")
        address = input("Enter address: ")
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.")

    def view_contact_list(self):
        if not self.contacts:
            print("No contacts in the list.")
        else:
            print("Contact List:")
            for i, contact in enumerate(self.contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def search_contact(self):
        search_term = input("Enter name or phone number to search: ")
        found_contacts = [contact for contact in self.contacts if search_term in contact.name or search_term in contact.phone_number]
        if not found_contacts:
            print("No contacts found.")
        else:
            print("Search Results:")
            for i, contact in enumerate(found_contacts, 1):
                print(f"{i}. {contact.name} - {contact.phone_number}")

    def update_contact(self):
        self.view_contact_list()
        contact_number = int(input("Enter the contact number to update: ")) - 1
        if contact_number < 0 or contact_number >= len(self.contacts):
            print("Invalid contact number.")
        else:
            contact = self.contacts[contact_number]
            print(f"Updating contact '{contact.name}':")
            contact.name = input("Enter new name: ")
            contact.phone_number = input("Enter new phone number: ")
            contact.email = input("Enter new email: ")
            contact.address = input("Enter new address: ")
            print(f"Contact '{contact.name}' updated successfully.")

    def delete_contact(self):
        self.view_contact_list()
        contact_number = int(input("Enter the contact number to delete: ")) - 1
        if contact_number < 0 or contact_number >= len(self.contacts):
            print("Invalid contact number.")
        else:
            contact = self.contacts.pop(contact_number)
            print(f"Contact '{contact.name}' deleted successfully.")

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Quit")

        choice = input("Choose an option: ")

        if choice == "1":
            contact_book.add_contact()
        elif choice == "2":
            contact_book.view_contact_list()
        elif choice == "3":
            contact_book.search_contact()
        elif choice == "4":
            contact_book.update_contact()
        elif choice == "5":
            contact_book.delete_contact()
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid option. Please choose again.")

if __name__ == "__main__":
    main()