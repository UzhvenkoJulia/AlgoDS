"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""

class BookEntry:
    # прямокутник зі стрілкою
    def __init__(self, author_name: str, book_title: str):
        self.author_name: str = author_name
        self.book_title: str = book_title
        self.next_entry: [None | BookEntry] = None  # type: ignore


size: int = 10_000
library_slots: list[None | BookEntry]


def __hash__(value: str):
    return hash(value) % size


def init():
    """ Викликається 1 раз на початку виконання програми. """
    
    global library_slots
    library_slots = [None for _ in range(size)]


def addBook(author_name, book_title):
    """ Додає книгу до бібліотеки.
    :param author_name: Автор книги
    :param book_title: Назва книги
    """
    
    index = __hash__(author_name)
    current_entry = library_slots[index]
    while current_entry is not None:
        if current_entry.author_name == author_name and current_entry.book_title == book_title:
            return
        current_entry = current_entry.next_entry

    new_entry = BookEntry(author_name, book_title)
    new_entry.next_entry = library_slots[index]
    library_slots[index] = new_entry


def find(author_name, book_title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author_name: Автор
    :param book_title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    
    index = __hash__(author_name)
    entry = library_slots[index]
    while entry is not None:
        if entry.author_name == author_name and entry.book_title == book_title:
            return True
        entry = entry.next_entry
    return False


def delete(author_name, book_title):
    """ Видаляє книгу з бібліотеки.
    :param author_name: Автор
    :param book_title: Назва книги
    """
    
    index = __hash__(author_name)
    entry = library_slots[index]
    if entry is None:
        return
    if entry.author_name == author_name and entry.book_title == book_title:
        library_slots[index] = entry.next_entry
        return

    previous_entry = entry
    entry = entry.next_entry
    while entry is not None:
        if entry.author_name == author_name and entry.book_title == book_title:
            previous_entry.next_entry = entry.next_entry
            return
        previous_entry = entry
        entry = entry.next_entry


def findByAuthor(author_name):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author_name: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    
    books_by_author = []
    index = __hash__(author_name)
    entry = library_slots[index]
    while entry is not None:
        if entry.author_name == author_name:
            books_by_author.append(entry.book_title)
        entry = entry.next_entry
    return books_by_author