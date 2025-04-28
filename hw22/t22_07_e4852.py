from collections import deque

n, x = map(int, input().split())

adj_matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    adj_matrix.append(row)

# -1 - вершина недосяжна
dist = [-1] * n

queue = deque()

# з 0, тому x-1
dist[x - 1] = 0
queue.append(x - 1)

while queue:
    current = queue.popleft()  
    for neighbor in range(n):  
        if adj_matrix[current][neighbor] == 1 and dist[neighbor] == -1:
            # якщо є ребро і сусід ще не відвіданий
            dist[neighbor] = dist[current] + 1 
            queue.append(neighbor)

# через пропуск
print(*dist)