n, m = map(int, input().split())  

edges = set()

for _ in range(m):
    u, v = map(int, input().split())  
    edge = (u, v)  
    if edge in edges:
        print("YES")
        break
    edges.add(edge)
else:
    print("NO")