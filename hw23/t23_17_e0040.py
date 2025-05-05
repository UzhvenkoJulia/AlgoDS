import sys
sys.setrecursionlimit(10000)


input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]
rev_graph = [[] for _ in range(n)]  # зворотний граф

for to_node in range(n):
    parts = list(map(int, input().split()))
    for from_node in parts[1:]:  # перше число - к-сть ребер
        from_node -= 1
        graph[from_node].append(to_node)
        rev_graph[to_node].append(from_node)

def dfs(u, visited, g):  # сильна зв'яз
    visited[u] = True
    for v in g[u]:
        if not visited[v]:
            dfs(v, visited, g)

def s_connected(g):
    visited = [False] * n
    dfs(0, visited, g)
    if not all(visited):
        return False
    rev = [[] for _ in range(n)]
    for u in range(n):
        for v in g[u]:
            rev[v].append(u)
    visited = [False] * n
    dfs(0, visited, rev)
    return all(visited)

# переорієнт інцидентні ребра
for v in range(n):
    new_graph = [[] for _ in range(n)]
    for u in range(n):
        for w in graph[u]:
            if u == v or w == v:
                continue
            new_graph[u].append(w)
    
    # ребра до v
    for u in range(n):
        if v in graph[u]:
            new_graph[v].append(u)  # змін напрямок
        if u in graph[v]:
            new_graph[u].append(v)
    
    if s_connected(new_graph):
        print(1)
        sys.exit(0)

print(0)