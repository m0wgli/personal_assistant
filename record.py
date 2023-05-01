from collections import UserDict
from datetime import datetime
import pickle
import pathlib
        
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


    def days_to_birthday(self, birthday):
        birthday = str(birthday)
        current_date = datetime.now().date()
        normal_date = datetime.strptime(birthday, '%d.%m.%Y').replace(
            year=current_date.year).date()
        days = (normal_date - current_date).days
        if days < 0:
            normal_date = datetime.strptime(birthday, '%d.%m.%Y').replace(
                year=current_date.year + 1).date()
            days = (normal_date - current_date).days
        self.records.append(f'days to BD = {days} ;')


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

    # def iterator(self, records_count=3):
    #     start_iterate = 0
    #     while True:
    #         if start_iterate >= len(self.data):
    #             break
    #         yield dict(islice(self.data.items(),
    #                           start_iterate,
    #                           start_iterate + records_count))
    #         start_iterate += records_count

    def save_to_bin(self, path="AddressBook.bin"):
        with open(path, "wb") as f:
            pickle.dump(self, f)

    @staticmethod
    def load_from_bin(path="AddressBook.bin"):
        if pathlib.Path(path).exists():
            with open(path, "rb") as f:
                return pickle.load(f)
        else:
            return AddressBook()

    

if __name__ == '__main__':
    contacts = AddressBook.load_from_bin()

    name = "vitala"
    name1 = 'Igor'

    address = '123123'
    address1 = 'asdasd'

    phone = '456456456'
    phone1 = 'rtyrtyrtyr'


    record = Record(name)
    record.add_address(address)
    record.add_phone(phone)
    record.add_phone(phone1)

    contacts.add_record(record)
    record.change_phone('456456456', '111')
    # record.change_address('qweq')
    # contacts.del_record(record)

    # record1 = Record(name1)
    # record1.add_phone(phone)

    # contacts.add_record(record1)
    # record1.change_address('nm,nm,')
    contacts.save_to_bin()
    print(contacts)