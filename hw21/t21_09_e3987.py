n, m = map(int, input().split())  

edges = set()

for _ in range(m):
    u, v = map(int, input().split()) 
    if u != v:  # щоб не було петель
        edges.add(tuple(sorted([u, v])))  # +пару, відсорт за номер верш

# чи к-сть унікальних ребер = max к-сті для повного графа
if len(edges) == (n * (n - 1)) // 2:
    print("YES")
else:
    print("NO")