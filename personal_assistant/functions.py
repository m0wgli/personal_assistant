# import colorama
# from termcolor import colored
from notebook import Note_book, Text, Keyword, RecordNote
from adressbook import Adress_book, Record, Name, Phone, Email, Birthday, Adress

from sorter import main as sort_main
# from dec import input_error

# import pickle
# colorama.init()

def hello():
    with open('hello.txt', 'rb') as fh:
        text = fh.read().decode('utf-8')
    return text

def help():
    with open('help.txt', 'rb') as fh:
        text = fh.read().decode('utf-8')
    return text

def sorter():
    sort_main()

def close():
    return 'До нових зустрічей!'

def add_note():
    tag = Keyword(input('Введи теги через кому або залиш поле порожнім:\n>>> '))
    text = Text(input('Введи текст нотатки:\n>>> '))
    record = RecordNote(text=text, keyword=tag)
    return Note_book.add_record(record)

def del_note():
    param = input('Введи тег для видалення нотатки:\n>>> ')
    note = Note_book.delete_note(param)
    Adress_book.save_to_bin()
    return note

def search_note():
    param = input('Введи слово для пошуку у нотатнику:\n>>> ')
    return Note_book.search(param)

def show_notes():
    
    return Note_book.show_all_notes()

def add_contact():
    name = Name(input('Введи ім\'я користувача>>> '))
    phone = Phone(input('Введи номер телефону користувача починаючи с +38>>> '))
    email = Email(input('Якщо в користувача є імел, то введи його тут або залиш поле порожнім>>> '))
    bd = Birthday(input('Напиши дату дня народження користувача у форматі дд-мм-рррр і я нагадаю тобі коли його потрібно привітати>>> '))
    ad = Adress(input('Також ти можеш додати адресу користувача, якщо звісно ж знаєш>>> '))
    rec = Record(name=name, phone=phone, email=email, birthday=bd, address=ad)
    Adress_book.add_record(rec)
    Adress_book.save_to_bin()
    return f'\nКонтакт {name.value} успішно створеною'


def note_book():
    # Note_book.load_from_bin()
    while True:
        user_input = input('\nВітаю в меню нотатника!\n\
Я вмію додавати(команда add) нотатки за тегами;\n\
видаляти(команда del) та редугавати нотатки(команда edit);\n\
здіснювати пошук за тегами(команда search);\n\
а також можу показати усі збережені записи(команда show).\n\
\n\
Щоб перейти до головного меню обери команду menu.\n\
>>> ').lower()
        
        match user_input:
            case 'add':
                print(add_note())        
            
            case 'del':
                print(del_note())            

            case 'edit':
                user_input = input('Що саме ти хочеш змінити? (тег чи текст нотатки)>>>')
                match user_input:
                    case 'тег':
                        pass
                    case 'текст':
                        pass

            case 'search':
                print(search_note())

            case 'show':
                print(show_notes())

            case 'menu':
                main()

            case _:
                print('Вибач, але в нотатнику поки що немає такої команди.')


def adress_book():
    while True:
        user_input = input('\nПривіт! Щоб додати контакт введи add;\n\
    видалити контакт за командою del;\
    \n\
    Щоб перейти до головного меню обери команду menu.\n\
    >>> ').lower()
        
        match user_input:
            case 'add':
                print(add_contact())
            case 'del':
                pass
            case 'edit':
                pass
            case 'show':
                pass
            case 'menu':
                main()
            case _:
                print('Вибач, але в записній книзі немає такої команди.')




COMMANDS = {
    help: 'help',
    note_book: 'notes',
    sorter: 'sort',
    close: 'exit',
    adress_book: 'contacts'
}


def no_command():
    return 'Вибач, але я поки що не знаю такої команди.'


def command_handler(text: str):
    for command, kword in COMMANDS.items():
        if text.startswith(kword):
            return command
    return no_command


def main():
    
    while True:
        user_input = input('\nТи у головному меню. Очікую команду від тебе:\n>>> ')
        command = command_handler(user_input)
        print(command())
        if command == close:
            raise SystemExit
            

if __name__ == '__main__':
    print(hello())
    main()
