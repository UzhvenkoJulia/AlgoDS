# Перевірка орфографії
# використання хеш-таблиці (set)

'''
import sys
import re
# використовується для роботи з регулярними виразами

data = sys.stdin.read().split("\n")

# зчитуємо перший рядок з N та M
N, M = map(int, data[0].split())

# зчитуємо словник (переводимо слова у нижній регістр)
dictionary = {data[i].strip().lower() for i in range(1, N + 1)}
# формуємо множину dictionary зі слів словника, переводячи їх у нижній регістр (lower())

found_words = set()

# регулярний вираз для виділення слів (рядкові та великі латинські літери)
word_pattern = re.compile(r"[a-zA-Z]+")
'''
'''
r"...": позначає, що рядок є сирим рядком (raw string). У сирому рядку символи екранування (наприклад, \) не мають спеціального значення, тому їх не потрібно подвоювати, як це робиться в звичайних рядках.

[a-zA-Z]: клас символів, який визначає, що ми шукаємо будь-яку букву англійського алфавіту.
a-z — будь-яка мала літера.
A-Z — будь-яка велика літера.

+: означає, що символи, визначені в попередньому класі (тобто букви), можуть повторюватися один або більше разів. Тобто буде знайдено слово з будь-якою кількістю літер.
'''
'''

# обробляємо текст твору, додаючи слова до множини
for i in range(N + 1, N + 1 + M):
    for word in word_pattern.findall(data[i]):
        # метод findall() повертає список усіх підрядків, що відповідають заданому патерну
        # findall() у модулі re (regular expressions) використовується для пошуку всіх збігів заданого регулярного виразу в рядку. 
        # Він повертає список усіх знайдених відповідностей.
        found_words.add(word.lower())  

if found_words == dictionary:
    print("Everything is going to be OK.")
elif not found_words.issubset(dictionary):
    # метод issubset() використовується для перевірки того, чи є одна множина підмножиною іншої
    print("Some words from the text are unknown.")
else:
    print("The usage of the vocabulary is not perfect.")
'''

import re
# імпорт модуля регулярних виразів

# Клас для реалізації хеш-таблиці
class HashTable:
    def __init__(self, size):
        self.size = size  # розмір хеш-таблиці
        self.table = [[] for _ in range(size)]  # масив списків для зберігання елементів

    def _hash_function(self, key):
        # хеш-функція: сума ASCII символів і взяття за модулем розміру таблиці
        return sum(ord(char) for char in key) % self.size

    def insert(self, key):
        index = self._hash_function(key)
        # чи ключ вже є в таблиці
        if key not in self.table[index]:
            self.table[index].append(key)

    def search(self, key):
        index = self._hash_function(key)
        return key in self.table[index]

    def __contains__(self, key):
        return self.search(key)

    def get_all_keys(self):
        # витягуємо всі ключі з хеш-таблиці у вигляді множини
        keys = set()
        for bucket in self.table:
            keys.update(bucket)
        return keys


# зчитуємо перші два числа: N (к-сть слів у словнику) та M (к-сть рядків у тексті)
N, M = map(int, input().split())

# створюємо хеш-таблицю для слів словника
dictionary = HashTable(1000)  

for _ in range(N):
    word = input().strip().lower()  
    dictionary.insert(word)  # вставляємо слово в хеш-таблицю

text_words = set()

# шаблон для виділення слів з тексту
pattern = r"[a-zA-Z]+"

for _ in range(M):
    line = input().strip().lower() 
    words_in_line = re.findall(pattern, line)  
    text_words.update(words_in_line)  

dictionary_words = dictionary.get_all_keys()

# перевіряємо умови
# перевірка на рівність множин: чи всі слова з тексту є в словнику і всі слова зі словника є в тексті
if text_words.issubset(dictionary_words) and dictionary_words.issubset(text_words):
    print("Everything is going to be OK.")
# чи всі слова з тексту є в словнику
elif text_words.issubset(dictionary_words):
    print("The usage of the vocabulary is not perfect.")
# якщо є слова в тексті, яких немає в словнику
else:
    print("Some words from the text are unknown.")
