# Зв`язні списки. Їхнє застосування.
# 15.7. Зміна порядку списку (100%)
# Вказівка 1. У кожному завданні має бути реалізований та використаний один з різновидів зв'язного списку 
# (однозв'язний, двозв`язний, кільцевий або з поточним елементом), навіть, якщо це суперечить вимогам задачі на порталі Eolymp.
# Вказівка 2. Забороняється використовувати будь-який масив 
# (list, tuple тощо) та довільне відображення (dict, set тощо) окрім блоку зчитування даних. 

import sys

class Node:

    def __init__(self, data: int):
        self.data: int = data  # значення вузла
        self.next: 'Node | None' = None  # посилання на наступний вузол

class List:

    def __init__(self):
        self.head: 'Node | None' = None  # початковий елемент списку
        self.tail: 'Node | None' = None  # кінцевий елемент списку
    
    def addToTail(self, val: int) -> None:

        """додає число val в кінець зв’язного списку"""

        new_node = Node(val)

        if self.tail:
            self.tail.next = new_node  # останній елемент тепер вказує на новий
        self.tail = new_node  

        if self.head is None:
            self.head = new_node  # якщо список був порожнім, оновл голову
    

    def ReorderList(self) -> None:

        """перегруповує список за вказаною схемою"""

        if not self.head or not self.head.next:
            return  # якщо список порожній або містить 1 елемент, змінювати нічого
        
        # 1. зн середину списку (швидкий та повільний вказівники)
        slow, fast = self.head, self.head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # 2. розбив список на дві половини та реверс другу половину
        prev, curr = None, slow.next
        slow.next = None  # закінч першу половину

        while curr:
            next_node = curr.next
            curr.next = prev
            prev = curr
            curr = next_node
        second_half = prev  # початок реверсованої другої половини
        
        # 3. черг елем з першої та другої половин
        first_half = self.head

        while second_half:
            tmp1, tmp2 = first_half.next, second_half.next
            first_half.next = second_half
            second_half.next = tmp1
            first_half = tmp1
            second_half = tmp2
    

    def Print(self) -> None:

        """виводить елементи зв’язного списку у потрібному форматі"""

        current = self.head

        while current:
            print(current.data, end=' ')
            current = current.next

        print()

def main():

    n = int(sys.stdin.readline().strip())  
    values = map(int, sys.stdin.readline().strip().split())  
    
    linked_list = List()
    
    for val in values:
        linked_list.addToTail(val)
    
    linked_list.ReorderList()
    linked_list.Print()

if __name__ == "__main__":
    main()