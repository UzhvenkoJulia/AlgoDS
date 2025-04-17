# 19.4. Черга з пріоритетами (100%)
# Двійкова купа та пріоритетна черга.
# Вказівка. Описати пріоритетну чергу на базі двійкової купи.
# Вказівка. У кожному завданні має бути реалізована та використана бінарна купа


import sys
input = sys.stdin.readline 

# пріоритетна черга на базі максимальної двійкової купи (max-heap)

class PriorityQueue:

    def __init__(self):
        self.heap = []                     
        self.id_to_index = {}  # id → індекс у купі

    def _swap(self, i, j):
        # обмін елементів у масиві heap і оновлення індексів у словнику
        self.id_to_index[self.heap[i][0]] = j
        self.id_to_index[self.heap[j][0]] = i
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

    def _sift_up(self, index):
        # піднімає елем вгору по купі, якщо він має більший пріоритет за батьків
        while index > 0:
            parent = (index - 1) // 2
            if self.heap[index][1] > self.heap[parent][1]: 
                self._swap(index, parent)
                index = parent
            else:
                break

    def _sift_down(self, index):
        # опускає елем вниз по купі, якщо його пріоритет менший за нащадків
        n = len(self.heap)

        while True:
            left = 2 * index + 1
            right = 2 * index + 2
            largest = index

            if left < n and self.heap[left][1] > self.heap[largest][1]:
                largest = left
            if right < n and self.heap[right][1] > self.heap[largest][1]:
                largest = right

            if largest != index:
                self._swap(index, largest)
                index = largest
            else:
                break

    def add(self, id, priority):
        self.heap.append((id, priority))           
        self.id_to_index[id] = len(self.heap) - 1  
        self._sift_up(len(self.heap) - 1)  # купу вгору

    def pop(self):
        top_id, top_priority = self.heap[0]     
        last = self.heap.pop()                     

        if self.heap:
            self.heap[0] = last                 
            self.id_to_index[last[0]] = 0
            self._sift_down(0)             

        del self.id_to_index[top_id]  # видал запис про індекс
        return top_id, top_priority 

    def change(self, id, new_priority):
        # змін пріоритет існуючого елементу
        index = self.id_to_index[id]              
        old_priority = self.heap[index][1]
        self.heap[index] = (id, new_priority)      

        if new_priority > old_priority:
            self._sift_up(index)
        else:
            self._sift_down(index)


pq = PriorityQueue()   

for line in sys.stdin:
    if not line.strip():
        continue
    parts = line.strip().split()

    if parts[0] == "ADD":
        id = parts[1]
        priority = int(parts[2])
        pq.add(id, priority)

    elif parts[0] == "POP":
        id, priority = pq.pop()
        print(f"{id} {priority}")

    elif parts[0] == "CHANGE":
        id = parts[1]
        new_priority = int(parts[2])
        pq.change(id, new_priority)