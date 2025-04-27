# Стек - базові алгоритми.
# Завдання для самостійної роботи
# 12.3. Стек із захистом від помилок (100%)
# Вказівка. У кожному завданні має бути реалізований та використаний стек.

import sys


class CustomStack:
    def __init__(self):
        self._items = []

    def push(self, n):
        self._items.append(n)
        return 'ok'

    def pop(self):
        if self.size() != 0:
            return self._items.pop()
        else:
            return 'error'

    def back(self):
        if self.size() != 0:
            return self._items[-1]  # повертає останній елемент з стека (який зараз знаходиться на вершині)
        else:
            return 'error'

    def size(self):
        return len(self._items)

    def clear(self):
        self._items.clear()
        return 'ok'

    @staticmethod
    def exit():
        return 'bye'

    def handle_command(self, command):  # динамічний виклик методів через getattr()
        parts = command.split()
        method = parts[0]  # перший елемент списку
        args = parts[1:]  # зріз списку, щоб отримати всі елементи після першого
        result = getattr(self, method)(*args)  # викликаємо метод
        print(result)  # дозволяє отримати атрибути (методи чи змінні) об'єкта за його іменем, яке задається як рядок

        if result == 'bye':
            sys.exit()  

        return result


def main():
    stack = CustomStack()
    with open('input.txt') as f:
        for line in f:
            stack.handle_command(line.strip())  

if __name__ == '__main__':
    main()
