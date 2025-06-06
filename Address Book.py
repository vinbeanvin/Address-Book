class Contact:
    def __init__(self, first_name, last_name, address, contact_number):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.contact_number = contact_number   

    def __str__(self):
        return f"{self.first_name} {self.last_name}, {self.address}, {self.contact_number}"

class AddressBook:
    def __init__(self):
        self.contacts = []
        
    def add_contact(self):
        if len(self.contacts) < 100:        
            first_name = input("Enter first name: ")
            last_name = input("Enter last name: ")
            address = input("Enter address: ")
            contact_number = input("Enter contact number: ")
            new_contact = Contact(first_name, last_name, address, contact_number)
            self.contacts.append(new_contact)     
            print(f"Contact added successfully.")
        else:
            print("Address book is full.")

    def edit_contact(self):
        entry_number = int(input("Enter the entry number you want to edit: ")) - 1
        if 0 <= entry_number < len(self.contacts):  
            contact = self.contacts[entry_number]
            print(f"Editing contact: {contact}")
            contact.first_name = input("Enter new first name: ")
            contact.last_name = input("Enter new last name: ")
            contact.address = input("Enter new address: ")
            contact.contact_number = input("Enter new contact number: ")
            print("Contact updated successfully.")
        else:
            print("Invalid entry number. Contact not found.")

    def delete_contact(self):
        entry_number = int(input("Enter the entry number you want to delete: ")) - 1
        if 0 <= entry_number < len(self.contacts):
            deleted_contact = self.contacts.pop(entry_number)
            print(f"Deleted contact: {deleted_contact}")
        else:
            print("Invalid entry number. Contact not found.")

    def view_contacts(self):
        for i, contact in enumerate(self.contacts, start=1):
            print(f"{i}. {contact}")

    def search_contacts(self, query):
        results = []
        for contact in self.contacts:
            if query in contact.first_name.lower() or query in contact.last_name.lower() or query in contact.address.lower() or query in contact.contact_number:
                results.append(contact)
        if len(results) == 0:
            print("No matching contacts found.")
        else:
            print("Contacts found:")
            for i, contact in enumerate(results):
                print(f"{i}: {contact.first_name} {contact.last_name}, {contact.address}, {contact.contact_number}")




if __name__ == "__main__":
    address_book = AddressBook()

    address_book.contacts.append(Contact("Ralph Andrei", "Castillo", "123 Buklod St.", "099112341234"))
    address_book.contacts.append(Contact("Arthur", "Morgan", "456 Elm St", "8944646"))
  
    while True:
        print("\n1. Add Contact\n2. Edit Contact\n3. Delete Contact\n4. View Contacts\n5. Search Address Book\n6. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            address_book.add_contact()
        elif choice == '2':
            address_book.edit_contact()
        elif choice == '3':
            address_book.delete_contact()
        elif choice == '4':
            address_book.view_contacts()
        elif choice == '5':
            search = input("Enter name, address, or contact number: ")
            address_book.search_contacts(search)
        elif choice == '6':
            print("Exiting the program.")
            break
        else:
            print("Invalid choice. Please select a valid option.")
