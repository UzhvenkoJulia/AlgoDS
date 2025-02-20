'''
# Використання хеш-таблиць.
# Контакти

# к-сть телефонних з'єднань
N = int(input().strip())  # приводимо вхідні дані до цілого числа та видаляємо зайві пробіли

# (set) для збереження унікальних номерів телефонів
contact_book = set()

# зчитуємо N телефонних номерів
phone_numbers = map(int, input().split())  # розбиваємо на числа та перетворюємо їх на int

# додаємо кожен номер до множини (хеш-таблиця автоматично уникає дублікатів)
for number in phone_numbers:
    contact_book.add(number)  

# виводимо к-сть унікальних записів у книзі контактів
print(len(contact_book))  # розмір множини = к-сті унікальних телефонних номерів
'''

'''
import sys
# надає функції та змінні для взаємодії з інтерпретатором Python та стандартними потоками введення/виведення

# зчитуємо вхідні дані
try:
    data = sys.stdin.read().split()  # читаємо всі вхідні дані одним викликом
    N = int(data[0])  # отримуємо кількість з'єднань

    # використовуємо словник (dict) як хеш-таблицю для збереження унікальних номерів
    contact_book = {}
    # вбудована структура, яка працює як асоціативний масив (хеш-таблиця)

    # заповнюємо хеш-таблицю унікальними номерами
    for phone_number in data[1:N+1]:  
        contact_book[phone_number] = True  

    print(len(contact_book))

except EOFError:
    print("помилка: неочікуваний кінець файлу")
'''

class HashTable:
    def __init__(self, size=100000):  # вибираємо просте число для розміру хеш-таблиці
        self.size = size
        self.table = [[] for _ in range(size)]
        # ініціалізація хеш-таблиці у вигляді списку списків (список бакетів)
        # для кожного значення в range(size) створюється порожній список []
        # ланцюгове хешування

    def _hash(self, key):
        """ хеш-функція для обчислення індексу """
        # _hash приймає key (номер телефону) та обчислює індекс для збереження
        # обчислення залишку від ділення дає індекс у межах 0 до size-1
        return key % self.size

    def insert(self, key):
        """ додає ключ до хеш-таблиці, якщо його ще немає """
        index = self._hash(key)
        if key not in self.table[index]:
            self.table[index].append(key)

    def count_unique(self):
        """ повертає к-сть унікальних елементів """
        return sum(len(bucket) for bucket in self.table)

def count_unique_contacts(n, phone_numbers):
    """
    підраховує к-сть унікальних номерів телефонів у книзі контактів.
    Використовується власна реалізація хеш-таблиці.
    
    :param n: к-сть телефонних з'єднань (1 ≤ N ≤ 100000)
    :param phone_numbers: список дев’ятизначних номерів телефонів
    :return: к-сть унікальних номерів у книзі контактів
    """
    contact_book = HashTable()  
    
    for number in phone_numbers:
        contact_book.insert(number)  # Додаємо номер до хеш-таблиці
    
    return contact_book.count_unique()  # к-сть унікальних номерів

n = int(input().strip())  # к-сть з'єднань
phone_numbers = list(map(int, input().strip().split()))  # список телефонних номерів

# отримуємо та виводимо к-сть унікальних контактів
print(count_unique_contacts(n, phone_numbers))
