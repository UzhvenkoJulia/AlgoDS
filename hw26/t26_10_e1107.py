import sys

INF = sys.maxsize

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
        return len(self.mItems) == 1

    def insert(self, key, priority):
        el = PQElement(key, priority)
        self.mSize += 1
        self.mItems.append(el)
        self.mElementsMap[key] = self.mSize
        self.siftUp()

    def extractMinimum(self):
        root = self.mItems[1].key()
        self.swap(1, -1)
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
        while (2 * i) <= self.mSize:
            left = 2 * i
            right = 2 * i + 1
            min_child = self.minChild(left, right)
            if self.mItems[i] > self.mItems[min_child]:
                self.swap(min_child, i)
            else:
                break
            i = min_child

    def siftUp(self):
        i = len(self.mItems) - 1
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            else:
                break
            i = parent

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
        self.mItems[i].updatePriority(priority)
        while i > 1:
            parent = i // 2
            if self.mItems[i] < self.mItems[parent]:
                self.swap(parent, i)
            else:
                break
            i = parent
        return True


class Graph:
    def __init__(self, n):
        self.n = n
        self.vertices = {i: {} for i in range(1, n + 1)}  # сусід: вага

    def add_edge(self, i, j, weight):  # двонапрямлений граф
        self.vertices[i][j] = weight
        self.vertices[j][i] = weight

    def prim(self, banned_edge=None):

        """ banned_edge - ребро (u,v) яке не враховується (для пошуку другого за вартістю мін дерева)"""

        weight_sum = 0
        
        costs = [INF] * (self.n + 1)
        parents = [-1] * (self.n + 1)
        in_mst = [False] * (self.n + 1)

        costs[1] = 0

        pq = PriorityQueue()
        for i in range(1, self.n + 1):
            pq.insert(i, costs[i])

        while not pq.empty():
            
            u = pq.extractMinimum()
            in_mst[u] = True
            weight_sum += costs[u]

            for v, w in self.vertices[u].items():
                if banned_edge is not None:  

                    if (u == banned_edge[0] and v == banned_edge[1]) or (u == banned_edge[1] and v == banned_edge[0]):  # заборонене - пропуск
                        continue

                if not in_mst[v] and w < costs[v]:
                    costs[v] = w
                    parents[v] = u
                    pq.updatePriority(v, w)

        if not all(in_mst[1:]):
            return INF, []  # не зв'яз - INF

        mst_edges = []

        for v in range(2, self.n + 1):
            mst_edges.append((parents[v], v))
        return weight_sum, mst_edges


if __name__ == "__main__":

    input_data = sys.stdin.read().strip().split('\n')
    n, m = map(int, input_data[0].split())

    graph = Graph(n)

    for i in range(1, m + 1):

        a, b, c = map(int, input_data[i].split())
        graph.add_edge(a, b, c)

    best_weight, best_mst_edges = graph.prim()

    second_best = INF
    # вилуч по одному ребру з мін -> щочь ще (альтирнатив)
    for edge in best_mst_edges:

        weight, _ = graph.prim(banned_edge=edge)

        if best_weight <= weight < second_best:
            second_best = weight

    print(best_weight, second_best)