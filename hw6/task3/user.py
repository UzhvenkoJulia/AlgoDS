"""
Реалізуйте каталог деякої бібліотеки.
Бібліотека може містити кілька книг одного автора.
"""


EMPTY = "EMPTY"
DELETED = "DELETED"

size: int = 10_000
count: int
authors: list[str]
titles: list[str]


def init():
    """ Викликається 1 раз на початку виконання програми. """
    global count, authors, titles
    count = 0
    authors = [EMPTY for _ in range(size)]
    titles = [EMPTY for _ in range(size)]


# % не підтримується для рядків
def __hash__(value: str):
    return hash(value) % size


def addBook(author, title):
    """ Додає книгу до бібліотеки.
    :param author: Автор книги
    :param title: Назва книги
    """
    global count
    i = __hash__(author)
    while authors[i] not in (EMPTY, DELETED):
        if authors[i] == author and titles[i] == title:
            return
        i = (i + 1) % size
    
    authors[i] = author
    titles[i] = title
    count += 1


def find(author, title):
    """ Перевірає чи міститься задана книга у бібліотеці.
    :param author: Автор
    :param title: Назва книги
    :return: True, якщо книга міститься у бібліотеці та False у іншому разі.
    """
    i = __hash__(author)
    while authors[i] is not EMPTY:
        if authors[i] == author and titles[i] == title:
            return True
        i = (i + 1) % size
    return False


def delete(author, title):
    """ Видаляє книгу з бібліотеки.
    :param author: Автор
    :param title: Назва книги
    """
    i = __hash__(author)
    while authors[i] is not EMPTY:
        if authors[i] == author and titles[i] == title:
            authors[i] = DELETED
            titles[i] = DELETED
            return
        i = (i + 1) % size


def findByAuthor(author):
    """ Повертає список книг заданого автора.
    Якщо бібліотека не міститься книг заданого автора, то підпрограма повертає порожній список.
    :param author: Автор
    :return: Список книг заданого автора у алфавітному порядку.
    """
    books = []
    i = __hash__(author)
    while authors[i] is not EMPTY:
        if authors[i] == author:
            books.append(titles[i])
        i = (i + 1) % size
    return sorted(books)