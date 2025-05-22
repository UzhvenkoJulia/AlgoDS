# має бути використаний алгоритм Беллмана-Форда
# Алгоритми на зважених графах.
# 25.7. Автобуси


import sys

n = int(input())  
d, v = map(int, input().split())  
r = int(input())  

INF = float('inf')
dist = [INF] * (n + 1)
dist[d] = 0 

edges = []  # (u, t_depart, v, t_arrive)

for _ in range(r):

    u, t_depart, w, t_arrive = map(int, input().split())
    # (звідки, коли, куди, коли прибуває)
    edges.append((u, t_depart, w, t_arrive))

# макс n-1 раз
for _ in range(n - 1):

    updated = False

    for u, t_depart, w, t_arrive in edges:
        
        if dist[u] <= t_depart and t_arrive < dist[w]:
            dist[w] = t_arrive
            updated = True

    if not updated:
        break 

print(dist[v] if dist[v] != INF else -1)