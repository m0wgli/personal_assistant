from collections import UserDict
from datetime import datetime
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




class SaveLoadFile:
    def save_to_file(self, file):
        with open(file, 'wb') as fh:
            pickle.dump(self.data, fh)


    def load_from_file(self, file):
        with open(file, 'rb') as fh:
            data = pickle.load(fh)
            return data
