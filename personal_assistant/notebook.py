from collections import UserDict
import pickle


class Text:

    def __init__(self, text):
        self.text = text

    def __repr__(self):
        return f"{self.text}"


class Keyword:

    def __init__(self, keyword):
        self.keyword = keyword

    def __repr__(self):
        return f"{self.keyword}"


class RecordNote:

    def __init__(self, text: Text = None, keyword: Keyword = None):
        self.texts = [text] if text else []
        self.keywords = [keyword] if keyword else []

    def add_note(self, text: Text):
        self.texts.append(text)

    def add_keywords(self, keyword: Keyword):
        self.keywords.append(keyword)

    def edit_note(self, new_text: Text):
        self.new_texts = [new_text] if new_text else []
        old_text = self.texts
        new_note = self.new_texts
        self.texts = self.new_texts
        return f"Текст нотатки змінено з {old_text} на {new_note}"

    def edit_keyword(self, new_keyword: Keyword):
        self.new_keywords = [new_keyword] if new_keyword else []
        old_keyword = self.keywords
        new_keyword = self.new_keywords
        self.keywords = self.new_keywords
        return f"Тег змінено з {old_keyword} на {new_keyword}"

    def __repr__(self):
        join_text = ", ".join(str(text) for text in self.texts)
        join_keyword = ", ".join(str(keyword) for keyword in self.keywords)
        return "\n" f"- {join_text}\n- Теги: {join_keyword}" "\n"


class Notebook(UserDict):

    def __init__(self):
        super().__init__()
        try:
            with open('notebook.bin', 'rb') as f:
                while True:
                    try:
                        record = pickle.load(f)
                    except EOFError:
                        break
        except FileNotFoundError:
            pass

    def add_record(self, record: RecordNote):
        with open("notebook.bin", "ab") as f:
            pickle.dump(record, f)
        name_note = f"Запис {len(self.data) + 1}"
        self.data[name_note] = record
        return 'Нотатку збережено.'

    def search(self, param):
        if len(param) < 3:
            return "Для здійснення пошуку треба ввести принаймні 3 символи."
        result = ""
        for key, value in self.items():
            if param.lower() in str(key).lower() or param.lower() in str(
                    value).lower():
                result += f"{key} {value}\n"
        if not result:
            return "Упс, нічого подібного не знайдено :("
        return result

    def delete_note(self, param):
        keys_to_delete = [key for key in self.keys() if param in key]
        if not keys_to_delete:
            return "Запису для видалення не знайдено. Якщо необхідно, спробуйте ще раз."
        for key in keys_to_delete:
            del self[key]
        return f"Видалено {len(keys_to_delete)} записів."

    def sorting_by_keyword(self):
        sorted_data = dict(
            sorted(self.data.items(),
                   key=lambda x: str(x[1].keywords).lower()))
        self.data = sorted_data
        return self.data

    def __repr__(self):
        output = ""
        for key, value in self.data.items():
            output += f"{key} {value}\n"
        return output

Note_book = Notebook()