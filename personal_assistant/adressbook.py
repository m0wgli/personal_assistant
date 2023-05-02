from collections import UserDict
from datetime import datetime
from pathlib import Path
import pickle
import re


class Field:
    def __init__(self, value) -> None:
        self._value = value

    @property
    def value(self):
        return self._value
    
    @value.setter
    def value(self, new_value) -> None:
        self._value = new_value


class Name(Field):
    def __init__(self, value) -> None:
        self.value = value
    
    @Field.value.setter
    def value(self, value: str) -> None:
        if not value:
            raise ValueError('The name can\'t be empty')
        if not value.isalpha():
            raise ValueError('Name must be a string, not decimal!')
        self._value = value
    

class Phone(Field):
    def __init__(self, value):
        self.value = value
 
    @Field.value.setter
    def value(self, value):
        if bool(re.match(r'^\+380\d{9}$', value)):
            self._value = [value]
        else:
            raise ValueError('The phone must be like +380123456789')


class Email(Field):
    def __init__(self, value) -> None:
        self.value = value

    @Field.value.setter
    def value(self, value):
        if bool(re.match(r'[a-zA-Z][a-zA-Z0-9._]+@\w+\.[a-z]{2,}', value)):
            self._value = value
        else:
            raise ValueError('Email may consist of Latin characters, numbers, and symbols . and _')


class Birthday(Field):
    def __init__(self, value) -> None:
        self.value = value

    @Field.value.setter
    def value(self, value):
        try:
            datetime.strptime(value, "%d-%m-%Y")
            self.__value = datetime.strptime(value, "%d-%m-%Y").date()
        except ValueError:
            raise ValueError("Data is not correct. Must be dd-mm-yyyy")


class Adress(Field):
    pass




class Record:
    def __init__(self, name, phone = None, email = None, birthday = None, address = None):
        self.name = name
        self.records = {'phone': []}
        self.phone = phone 
        self.birthday = birthday
        self.email = email
        self.address = address


    def add_address(self, address):
        self.records['address'] = address

    def add_birthday(self, birthday):
        self.records['birthday'] = birthday


    def add_email(self, email):
        self.records['email'] = email


    def add_phone(self, phone):
        self.records['phone'].append(phone)



    def change_address(self, address):
        self.records['address'] = address


    def change_birthday(self, birthday):
        self.records['birthday'] = birthday


    def change_email(self, email):
        self.records['email'] = email


    def change_phone(self, old_phone, new_phone):
        if old_phone in self.records['phone']:
            index = self.records['phone'].index(old_phone)
            self.records['phone'][index] = new_phone
            print(f"Changed {old_phone} to {new_phone}")
        else:
            print(f"{old_phone} not found in self.records")



    def delete_address(self):
        del self.records['address']


    def delete_birthday(self):
        del self.records['birthday']


    def delete_email(self):
        del self.records['email']


    def delete_phone(self, phone):
        if phone in self.records['phone']:
            self.records['phone'].remove(phone)
            print(f"Deleted {phone}")
        else:
            print(f"{phone} not found in self.records")


    # def days_to_birthday(self, birthday):
    #     birthday = str(birthday)
    #     current_date = datetime.now().date()
    #     normal_date = datetime.strptime(birthday, '%d.%m.%Y').replace(
    #         year=current_date.year).date()
    #     days = (normal_date - current_date).days
    #     if days < 0:
    #         normal_date = datetime.strptime(birthday, '%d.%m.%Y').replace(
    #             year=current_date.year + 1).date()
    #         days = (normal_date - current_date).days
    #     self.records.append(f'days to BD = {days} ;')


    def __repr__(self):
        attrs = []
        attrs.append(f"{self.records}")
        return f"{', '.join(attrs)}"


class AddressBook(UserDict):
    def add_record(self, record):
        name = record.name
        self.data[name] = record
    
    def del_record(self, record):
        name = record.name
        self.data.pop(name)

    def save_to_bin(self, path="AddressBook.bin"):
        with open(path, "ab") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_bin(path="AddressBook.bin"):
        if Path(path).exists():
            with open(path, "rb") as f:
                return pickle.load(f)
        else:
            return AddressBook()
        
Adress_book = AddressBook()