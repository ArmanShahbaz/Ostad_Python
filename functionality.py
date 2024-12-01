import os
import fileHandler,validation
filePath = os.path.join(os.getcwd(), 'contactBook.csv')
fileHandler.write(filePath, [])  # Create the file if it doesn't exist

def saveContact():
    name = input("Name : ")
    while True:
        phone = input("Enter phone: ")
        if validation.validate_phone(phone):
            break
    while True:
        email = input("Enter email: ")
        if validation.validate_email(email):
            break
    address = input("Address : ")

    duplicate = fileHandler.is_duplicate(filePath, phone, email)
    if duplicate:
        print(f"Error: {duplicate}")
        return

    contact = fileHandler.load(filePath)
    row = {'name': name, 'number': phone, 'email' : email, 'address' : address }
    contact.append(row)
    fileHandler.write(filePath, contact)
    print("New contact saved successfully")

def deleteContact():
    name = input("Name: ")
    while True:
        phone = input("Enter phone: ")
        if validation.validate_phone(phone):
            break
   
    contacts =fileHandler.load(filePath) 

    matchData = {'name' : name, 'number' : phone}
    updatedData = [row for row in contacts if not all(row[field] == matchData[field] for field in matchData)]

    if len(contacts) == len(updatedData):
        print("\n Found no match foe deletion")
        return
    
    fileHandler.write(filePath,updatedData)
    print(f'\nCOntact ->{matchData} is Deleted ')


def showContacts():
    contacts = fileHandler.load(filePath)
    print("\n")
    if contacts:
        print(f"{'S.No':<5} {'Name':<15}{'Phone':<15}{'Email':<25}{'Address':<100}")
        print("-" * 160)
        for i, row in enumerate(contacts, start=1):
            print(f"{i:<5}{row['name']:<15}{row['number']:<15}{row['email']:<25}{row['address']:<100}")
    else:
        print("\nThe Phonebook is empty!")


def search():
    search_key = input("Enter Name or Phone Number to search: ").strip()
    contacts = fileHandler.load(filePath)

    # Search for matches
    results = [
        row for row in contacts
        if search_key.lower() in row['name'].lower() or search_key == row['number']
    ]

    # Display results
    if results:
        print("\nSearch Results:")
        print(f"{'S.No':<5} {'Name':<15}{'Phone':<15}{'Email':<25}{'Address':<100}")
        print("-" * 160)
        for i, row in enumerate(results, start=1):
            print(f"{i:<5}{row['name']:<15}{row['number']:<15}{row['email']:<25}{row['address']:<100}")
    else:
        print("\nNo matching contact found.")
