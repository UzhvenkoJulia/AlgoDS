# # Алгоритм Прима побудови каркасного дерева.
# # 26.3. Дорога 


import sys

INF = sys.maxsize

# input = sys.stdin.readline

# # пріоритет ч
# class Heap:
    
#     def __init__(self):
#         self.heap = []

#     def push(self, val): # вгору
#         self.heap.append(val)
#         self._sift_up(len(self.heap) - 1)

#     def pop(self): # вниз
#         if not self.heap:

#             return None
        
#         self._swap(0, len(self.heap) - 1)
#         val = self.heap.pop()
#         self._sift_down(0)
#         return val

#     def _sift_up(self, idx):
#         parent = (idx - 1) // 2
#         while idx > 0 and self.heap[idx][0] < self.heap[parent][0]:
#             self._swap(idx, parent)
#             idx = parent
#             parent = (idx - 1) // 2

#     def _sift_down(self, idx):
#         n = len(self.heap)

#         while True:

#             left = 2 * idx + 1
#             right = 2 * idx + 2
#             smallest = idx

#             if left < n and self.heap[left][0] < self.heap[smallest][0]:
#                 smallest = left
#             if right < n and self.heap[right][0] < self.heap[smallest][0]:
#                 smallest = right
#             if smallest == idx:
#                 break
#             self._swap(idx, smallest)
#             idx = smallest

#     def _swap(self, i, j):
#         self.heap[i], self.heap[j] = self.heap[j], self.heap[i]

#     def empty(self):
#         return len(self.heap) == 0

# t = int(input())
# for _ in range(t):
#     n, m, p, q = map(int, input().split())

#     p -= 1
#     q -= 1

#     graph = [[] for _ in range(n)]
#     for _ in range(m):

#         u, v, w = map(int, input().split())
#         u -= 1
#         v -= 1
#         graph[u].append((w, v))
#         graph[v].append((w, u))

#     visited = [False]*n # вже під'єднані
#     mst_edges = set()

#     visited[0] = True
#     heap = Heap()

#     for w, to in graph[0]:
#         heap.push((w, 0, to))

#     count = 1

#     while not heap.empty() and count < n:
#         w, u, v = heap.pop()

#         if not visited[v]:

#             visited[v] = True
#             count += 1
#             mst_edges.add((min(u, v), max(u, v)))
#             for w_next, to_next in graph[v]:
#                 if not visited[to_next]:
#                     heap.push((w_next, v, to_next))

#     if (min(p, q), max(p, q)) in mst_edges:
#         print("YES")
#     else:
#         print("NO")


class PQElement:
    def __init__(self, key=None, priority=INF):
        self.mKey = key
        self.mPriority = priority

    def updatePriority(self, priority):
        self.mPriority = priority

    def key(self):
        return self.mKey

    def __le__(self, other):
        return self.mPriority <= other.mPriority

    def __lt__(self, other):
        return self.mPriority < other.mPriority

    def __gt__(self, other):
        return self.mPriority > other.mPriority

    def __ge__(self, other):
        return self.mPriority >= other.mPriority

class PriorityQueue:
    def __init__(self):
        self.mItems = [PQElement(0, 0)]
        self.mSize = 0
        self.mElementsMap = {}

    def empty(self):
        return self.mSize == 0

    def insert(self, key, priority):
        el = PQElement(key, priority)
        self.mSize += 1
        self.mItems.append(el)
        self.mElementsMap[key] = self.mSize
        self.siftUp()

    def extractMinimum(self):
        root = self.mItems[1].key()
        self.swap(1, self.mSize)
        self.mItems.pop()
        del self.mElementsMap[root]
        self.mSize -= 1
        self.siftDown()
        return root

    def swap(self, i, j):
        pos_i = self.mItems[i].key()
        pos_j = self.mItems[j].key()
        self.mElementsMap[pos_i] = j
        self.mElementsMap[pos_j] = i
        self.mItems[i], self.mItems[j] = self.mItems[j], self.mItems[i]

    def siftDown(self):
        i = 1
        while 2*i <= self.mSize:
            left = 2*i
            right = 2*i + 1
            min_child = self.minChild(left, right)
            if self.mItems[i] > self.mItems[min_child]:
                self.swap(i, min_child)
                i = min_child
            else:
                break

    def siftUp(self):
        i = self.mSize
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break

    def minChild(self, left_child, right_child):
        if right_child > self.mSize:
            return left_child
        else:
            if self.mItems[left_child] < self.mItems[right_child]:
                return left_child
            else:
                return right_child

    def __contains__(self, item):
        return item in self.mElementsMap

    def updatePriority(self, key, priority):
        i = self.mElementsMap[key]
        if self.mItems[i].mPriority > priority:
            self.mItems[i].updatePriority(priority)
            self.siftUpFrom(i)

    def siftUpFrom(self, i):
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(i, parent)
                i = parent
            else:
                break


class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = {i: {} for i in range(1, n + 1)}

    def add_edge(self, u, v, w):
        self.vertices[u][v] = w
        self.vertices[v][u] = w

    def prim(self, p, q):
        parent = [-1] * (self.n + 1)  # збереження ребер
        costs = [INF] * (self.n + 1)
        costs[1] = 0

        queue = PriorityQueue()
        for i in range(1, self.n + 1):
            queue.insert(i, costs[i])

        while not queue.empty():
            u = queue.extractMinimum()
            for v in self.vertices[u]:
                if v in queue and self.vertices[u][v] < costs[v]:
                    costs[v] = self.vertices[u][v]
                    parent[v] = u  # зв’язок
                    queue.updatePriority(v, costs[v])

        # ребро (p, q) 
        # parent[i], i, i = 2, ..., n
        for i in range(2, self.n + 1):
            u = parent[i]
            v = i
            if (u == p and v == q) or (u == q and v == p):
                return "YES"
        return "NO"


def main():
    input = sys.stdin.readline
    t = int(input())
    for _ in range(t):
        n, m, p, q = map(int, input().split())
        graph = Graph(n)
        for __ in range(m):
            u, v, w = map(int, input().split())
            graph.add_edge(u, v, w)
        print(graph.prim(p, q))


if __name__ == "__main__":
    main()