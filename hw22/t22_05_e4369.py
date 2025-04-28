# Алгоритми на незважених графах. Обхід в ширину та глибину.
# 22.5. Підпал (100%)

from collections import deque

n, m = map(int, input().split())

# список суміжності 
graph = [[] for _ in range(n + 1)]  # вершини нумеруються з 1

for _ in range(m):  # ребра
    u, v = map(int, input().split())
    graph[u].append(v)  
    graph[v].append(u)  # граф незважений !!

k = int(input())
start_vertices = list(map(int, input().split()))

# -1 - вершина ще не горить
# dist[v] = час, коли вершина v загориться
dist = [-1] * (n + 1)

# BFS обхід у ширину
queue = deque()

for vertex in start_vertices:
    dist[vertex] = 0
    queue.append(vertex)

while queue:
    current = queue.popleft()  # вершина з черги
    for neighbor in graph[current]:  
        if dist[neighbor] == -1:  # якщо сусід ще не горить
            dist[neighbor] = dist[current] + 1  
            queue.append(neighbor)  

max_time = -1
vertex_with_max_time = -1

for v in range(1, n + 1):  
    if dist[v] > max_time:
        max_time = dist[v]
        vertex_with_max_time = v
    elif dist[v] == max_time and v < vertex_with_max_time:
        # якщо є кілька вершин з однаковим макс часом -> вершина із меншим номером
        vertex_with_max_time = v

print(max_time)
print(vertex_with_max_time)