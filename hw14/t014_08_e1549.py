# Черга та дек. Їхнє застосування.
# 14.8. Варварські племена (60%)
# Вказівка. У кожному завданні має бути використана черга або дек.

class Node:
    def __init__(self, value):
        self.value = value  # значення вузла (служниця G або K)
        self.next = None  

class CircularDeque:
    def __init__(self):
        self.tail = None  # останній елемент дека (кільця)
        self.size = 0  

    def push_back(self, value):
        new_node = Node(value)
        if self.size == 0:
            new_node.next = new_node  
            self.tail = new_node
        else:
            new_node.next = self.tail.next  # новий елемент вказує на голову
            self.tail.next = new_node  # старий хвіст вказує на новий елемент
            self.tail = new_node  
        self.size += 1

    def pop_front(self):
        if self.size == 0:
            return None
        head = self.tail.next  
        if self.size == 1:
            self.tail = None  # дек стає порожнім
        else:
            self.tail.next = head.next  # перест голову
        self.size -= 1
        return head.value

    def advance(self, steps):
        for _ in range(steps):
            self.tail = self.tail.next  # рух вперед по кільцю

    def get_front(self):
        return self.tail.next.value if self.size > 0 else None


def ritual(n, m, k):
    tribe_deque = CircularDeque()
    
    for i in range(1, n + 1):
        tribe_deque.push_back(('G', i))
    for i in range(1, m + 1):
        tribe_deque.push_back(('K', i + n))
    
    while tribe_deque.size > 1:
        # знаходжу першу жертву
        tribe_deque.advance(k - 1)
        first_victim = tribe_deque.pop_front()
        
        # друга жертва
        tribe_deque.advance(k - 1)
        second_victim = tribe_deque.pop_front()
        
        # плем'я нової служниці
        new_tribe = 'G' if first_victim[0] == second_victim[0] else 'K'
        new_index = (n + m) + 1  # номер нової служниці
        tribe_deque.push_back((new_tribe, new_index))
        n += 1  # збільш загальну к-сть служниць
    
    return "Gared" if tribe_deque.get_front()[0] == 'G' else "Keka"


results = []
while True:
    n, m, k = map(int, input().split())
    if n == 0 and m == 0 and k == 0:
        break
    results.append(ritual(n, m, k))

for res in results:
    print(res)