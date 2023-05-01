from notebook import Note_book, Text, Keyword, RecordNote, Notebook
from classes import Name, Phone, Email, Birthday, Adress
# from main inport main as command_main

from sorter import main as sort_main


def hello():
    with open('hello.txt', 'rb') as fh:
        text = fh.read().decode('utf-8')
    return text


def help():
    with open('help.txt', 'rb') as fh:
        text = fh.read().decode('utf-8')
    return text



def note_book():
    user_input = input('\nЯ вмію додавати(команда add) нотатки за тегами;\n\
видаляти(команда del) та редугавати нотатки(команда edit);\n\
здіснювати пошук за тегами(команда search);\n\
а також можу показати усі збережені записи(команда show).\n\
\n\
Щоб перейти до головного меню обери команду menu.\n\
>>> ').lower()
    
    match user_input:
        case 'add':
            tag = Keyword(input('Введи теги через кому або залиш поле порожнім:\n>>> '))
            text = Text(input('Введи текст нотатки:\n>>> '))
            record = RecordNote()
            record.add_keywords(tag)
            record.add_note(text)
            return Note_book.add_record(record)
        
        case 'del':
            param = input('Введи тег для видалення нотатки:\n>>> ')
            note = Note_book.delete_note(param)
            return note

        case 'edit':
            pass

        case 'search':
            param = input('Введи слово для пошуку у нотатнику:\n>>> ')
            note = Note_book.search(param)
            return note

        case 'show':
            pass

        case 'menu':
            pass

        case _:
            return 'Вибач, але я поки що не знаю такої команди.'


def adress_book():
    
    pass


def sorter():
    sort_main()



print(hello())
print(sorter())
