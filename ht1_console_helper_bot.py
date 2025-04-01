from collections import UserDict
import re

# Base Field class 
class Field:
    def __init__(self, value) -> str: # Class init
        self.value = value

    def __str__(self): 
        return str(self.value)

# Name class with validation
class Name(Field):
    def __init__(self, value): # Class init
        self.validate(value)
        super().__init__(value)

    def validate(self, value) -> str: # Validate name value
        if not value or not value.isalpha():
            raise ValueError("Name must contain only letters.")
        return value.capitalize() # Return mane with capital first letter
    
# Phone class with validation
class Phone(Field):
    def __init__(self, value): # Class init
        self.validate(value)
        super().__init__(value)

    def validate(self, value): # Validate phone value
        if not re.fullmatch(r"\d{10}", value):
            raise ValueError("Phone number must be exactly 10 digits.")

# Record class
class Record:
    def __init__(self, name): # Class init
        self.name = Name(name)
        self.phones = []

    # Add phone function
    def add_phone(self, phone):
        self.phones.append(Phone(phone))

    # Del phone function
    def delete_phone(self, phone) -> bool:
        for p in self.phones:
            if p.value == phone:
                self.phones.remove(p)
                return True
        return False

    # Edit phone function
    def edit_phone(self, old_phone, new_phone) -> bool:
        for i, p in enumerate(self.phones):
            if p.value == old_phone:
                self.phones[i] = Phone(new_phone)
                return True
        return False

    # Find phone function
    def find_phone(self, phone) -> str:
        for p in self.phones:
            if p.value == phone:
                return p
        return None

    def __str__(self):
        return f"Contact name: {self.name.value}, phones: {'; '.join(p.value for p in self.phones)}"

# Address book class
class AddressBook(UserDict):
    def add_record(self, record) -> str: # Add record
        self.data[record.name.value] = record

    def find(self, name) -> str: # find record
        return self.data.get(name)

    def delete(self, name): # Del record
        if name in self.data:
            del self.data[name]

if __name__=="__main__":
    
    # Create new address book
    book = AddressBook()

    # Create Rambo record
    john_record = Record("John")
    john_record.add_phone("1234567890")
    john_record.add_phone("5555555555")

    # Add John to address book
    book.add_record(john_record)

    # Create and add Jane
    jane_record = Record("Jane")
    jane_record.add_phone("9876543210")
    book.add_record(jane_record)

    # Print address book
    for name, record in book.data.items():
        print(record)

    # Edit John
    john = book.find("John")
    john.edit_phone("1234567890", "1112223333")

    print(john)  

    # Search John phone
    found_phone = john.find_phone("5555555555")
    print(f"{john.name}: {found_phone}")  

    # Del Jane
    book.delete("Jane")

    # Print address book again
    for name, record in book.data.items():
        print(record)