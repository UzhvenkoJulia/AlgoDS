# Алгоритми на зважених графах.
# Вказівка 1. Хоча б в одному завданні має бути використаний алгоритм Беллмана-Форда.
# Вказівка 2. Хоча б в одному завданні має бути використаний алгоритм Дейкстри.
# 25.3. Алгоритм Дейкстри (100%)

INF = 10**9  

def way(matrix, start, end):

    n = len(matrix)

    distances = [INF] * n
    visited = [False] * n
    distances[start] = 0

    for _ in range(n): 
        min_dist = INF
        u = -1  # не відвідана вершина

        for i in range(n):
            if not visited[i] and distances[i] < min_dist:
                min_dist = distances[i]
                u = i

        if u == -1:
            break 

        visited[u] = True

        for v in range(n):
            weight = matrix[u][v]

            if weight != -1 and not visited[v]:
                if distances[v] > distances[u] + weight:
                    distances[v] = distances[u] + weight

    return distances[end] if distances[end] != INF else -1

n, s, f = map(int, input().split())

s -= 1  # з 0
f -= 1

matrix = []

for _ in range(n):
    row = list(map(int, input().split()))
    matrix.append(row)

print(way(matrix, s, f))
