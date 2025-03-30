# Черга та дек. Їхнє застосування.
# Вказівка. Реалізувати чергу як рекурсивну структуру.
# Вказівка. У кожному завданні має бути використана черга або дек.
# Черга з захистом від помилок

class QueueNode:

    """
    вузол рекурсивної черги, містить значення і посилання на наступний елемент
    """

    def __init__(self, value, next_node=None):
        self.value = value
        self.next = next_node

class Queue:
    # черга як рекурсивна структура
    def __init__(self):
        self.front_node = None  # перший
        self.rear_node = None   # останній
        self._size = 0  
    
    def push(self, n):
        # додає елемент у кінець черги
        new_node = QueueNode(n)
        if self.rear_node:
            self.rear_node.next = new_node
        self.rear_node = new_node
        if not self.front_node:
            self.front_node = new_node
        self._size += 1
        print("ok")
    
    def pop(self):
        # вдаляє перший елемент і виводить його значення
        if self.front_node is None:
            print("error")
        else:
            print(self.front_node.value)
            self.front_node = self.front_node.next
            if self.front_node is None:
                self.rear_node = None  # якщо черга стала порожньою
            self._size -= 1
    
    def front(self):
        # виводить значення першого елемента без видалення
        if self.front_node is None:
            print("error")
        else:
            print(self.front_node.value)
    
    def size(self):
        print(self._size)
    
    def clear(self):
        self.front_node = None
        self.rear_node = None
        self._size = 0
        print("ok")
    
    def exit(self):
        print("bye")
        exit()

queue = Queue()

while True:
    
    command = input().strip().split()
    if command[0] == "push":
        queue.push(int(command[1]))
    elif command[0] == "pop":
        queue.pop()
    elif command[0] == "front":
        queue.front()
    elif command[0] == "size":
        queue.size()
    elif command[0] == "clear":
        queue.clear()
    elif command[0] == "exit":
        queue.exit()