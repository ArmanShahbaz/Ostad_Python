import functionality

def main():
    while True:
        print("\n--- Contact Book Menu ---")
        print("1. Add Contact")
        print("2. Delete Contact")
        print("3. Show All Contacts")
        print("4. Search Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            functionality.saveContact()
        elif choice == '2':
            functionality.deleteContact()
        elif choice == '3':
            functionality.showContacts()
        elif choice == '4':
            functionality.search()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()