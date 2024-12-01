import csv

# Load data
fieldNames = ['name', 'number', 'email', 'address'] 

def load(filePath):
    try:
        with open(filePath,'r') as contactBook:
            reader = csv.DictReader(contactBook)
            data = list(reader)
            return data
    except FileNotFoundError:
        print("\nSomthing went wrong with the file")

#  write data

def write(filePath,data):
    try:
            with open(filePath, 'w', newline='') as file:
                csv_writer = csv.DictWriter(file, fieldnames=fieldNames)
                csv_writer.writeheader()
                csv_writer.writerows(data)

    except Exception as e:
            print("\nSomething went wrong, try again later.")
            
    
   

def is_duplicate(filePath, phone, email):
    contacts = load(filePath)
    for contact in contacts:
        if contact['number'] == phone:
            return "\nPhone number already exists."
        if contact['email'] == email:
            return "\nEmail already exists."
    return None