class Contact:
    def __init__(self, name, phone_number, email, address):
        self.name = name
        self.phone_number = phone_number
        self.email = email
        self.address = address
    
    def __str__(self):
        return f"Name: {self.name}\nPhone Number: {self.phone_number}\nEmail: {self.email}\nAddress: {self.address}\n"

class ContactManager:
    def __init__(self):
        self.contacts = []
    
    def add_contact(self, name, phone_number, email, address):
        contact = Contact(name, phone_number, email, address)
        self.contacts.append(contact)
        print(f"Contact '{name}' added successfully.\n")
    
    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.\n")
        else:
            print("Contact List:")
            for index, contact in enumerate(self.contacts, start=1):
                print(f"Contact {index}:")
                print(contact)
    
    def search_contacts(self, search_term):
        found = False
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                print(contact)
                found = True
        if not found:
            print("No matching contacts found.\n")
    
    def update_contact(self, search_term):
        found_contact = None
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                found_contact = contact
                break
        
        if found_contact:
            print(f"Current details for contact '{found_contact.name}':")
            print(found_contact)
            print("Enter new details:")
            new_name = input("New Name: ").strip()
            new_phone_number = input("New Phone Number: ").strip()
            new_email = input("New Email: ").strip()
            new_address = input("New Address: ").strip()
            
            if new_name:
                found_contact.name = new_name
            if new_phone_number:
                found_contact.phone_number = new_phone_number
            if new_email:
                found_contact.email = new_email
            if new_address:
                found_contact.address = new_address
            
            print(f"Contact '{found_contact.name}' updated successfully.\n")
        else:
            print("Contact not found.\n")
    
    def delete_contact(self, search_term):
        deleted = False
        for contact in self.contacts:
            if (search_term.lower() in contact.name.lower()) or (search_term in contact.phone_number):
                self.contacts.remove(contact)
                print(f"Contact '{contact.name}' deleted successfully.\n")
                deleted = True
                break
        
        if not deleted:
            print("Contact not found.\n")

def main():
    contact_manager = ContactManager()
    
    while True:
        print("Welcome to the Contact Management System")
        print("1. Add a New Contact")
        print("2. View All Contacts")
        print("3. Search for a Contact")
        print("4. Update a Contact")
        print("5. Delete a Contact")
        print("6. Exit")
        
        choice = input("Enter your choice (1-6): ").strip()
        
        if choice == '1':
            name = input("Enter Name: ").strip()
            phone_number = input("Enter Phone Number: ").strip()
            email = input("Enter Email: ").strip()
            address = input("Enter Address: ").strip()
            contact_manager.add_contact(name, phone_number, email, address)
        
        elif choice == '2':
            contact_manager.view_contacts()
        
        elif choice == '3':
            search_term = input("Enter name or phone number to search: ").strip()
            contact_manager.search_contacts(search_term)
        
        elif choice == '4':
            search_term = input("Enter name or phone number of the contact to update: ").strip()
            contact_manager.update_contact(search_term)
        
        elif choice == '5':
            search_term = input("Enter name or phone number of the contact to delete: ").strip()
            contact_manager.delete_contact(search_term)
        
        elif choice == '6':
            print("Exiting Contact Management System. Goodbye!")
            break
        
        else:
            print("Invalid choice. Please enter a number from 1 to 6.\n")

# Run the main function
if __name__ == "__main__":
    main()
