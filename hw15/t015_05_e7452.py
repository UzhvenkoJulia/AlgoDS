# Зв`язні списки. Їхнє застосування.
# 15.5. Виведення зв’язного списку (100%)
# Вказівка 1. У кожному завданні має бути реалізований та використаний один з різновидів зв'язного списку 
# (однозв'язний, двозв`язний, кільцевий або з поточним елементом), навіть, якщо це суперечить вимогам задачі на порталі Eolymp.
# Вказівка 2. Забороняється використовувати будь-який масив 
# (list, tuple тощо) та довільне відображення (dict, set тощо) окрім блоку зчитування даних. 

class Node:
    def __init__(self, data: int):

        """
        клас для вузла однозв'язного списку
        """

        self.data: int = data  
        self.next: 'Node | None' = None  # посилання на наступний вузол
        # Node | None — це синтаксис для анотації типів у Python, який означає, що змінна може бути або об'єктом класу Node, або None

class List:

    def __init__(self):
        self.head: 'Node | None' = None  # головний елемент списку
        self.tail: 'Node | None' = None  # хвіст списку для швидкого додавання

    def addToTail(self, val: int) -> None:

        """
        додає новий елемент у кінець списку
        :param val: значення, яке додається в список
        """

        new_node = Node(val)  # новий вузол
        if self.tail is None:
            # якщо список порожній, то новий вузол стає і головою, і хвостом
            self.head = self.tail = new_node
        else:
            # + новий вузол в кінець і змінюємо tail
            self.tail.next = new_node
            self.tail = new_node


    def Print(self) -> None:

        """
        виводить елементи списку в прямому порядку
        """

        current = self.head

        while current:

            print(current.data, end=" ")

            current = current.next  # -> до наступного вузла

        print() 


    def PrintReverse(self) -> None:

        """
        виводить елементи списку в зворотному порядку
        """

        def recursive_print(node: 'Node | None') -> None:

            if node is None:
                return
            
            recursive_print(node.next)

            print(node.data, end=" ")
        
        recursive_print(self.head)
        
        print()

n = int(input())  
values = map(int, input().split())  

linked_list = List()

for val in values:
    linked_list.addToTail(val)

linked_list.Print()
linked_list.PrintReverse()