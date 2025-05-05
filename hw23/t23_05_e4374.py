# Топологічне сортування. Зв'язність графів.
# 23.5. Зв`язність графа (23%)

def dfs(u, adjacency, visited, r_edges):
    visited[u] = True
    for i in range(len(adjacency[u])):
        v, eid = adjacency[u][i]
        if not visited[v] and not r_edges[eid]:
            dfs(v, adjacency, visited, r_edges)

def main():
    N, M = map(int, input().split())

    edge_list = [None] * (M + 1)  # edge_list[1] .. edge_list[M]
    adjacency = [[] for _ in range(N + 1)]  # з 1 по N - суміжності

    for i in range(1, M + 1):
        a, b = map(int, input().split())

        edge_list[i] = (a, b)
        adjacency[a].append((b, i))
        adjacency[b].append((a, i))

    K = int(input())

    for _ in range(K):
        parts = list(map(int, input().split()))
        C = parts[0]
        r_edges = [False] * (M + 1)
        for j in range(1, C + 1):
            r_edges[parts[j]] = True

        visited = [False] * (N + 1)

        dfs(1, adjacency, visited, r_edges)

        connected = True
        for i in range(1, N + 1):
            if not visited[i]:
                connected = False
                break

        if connected:
            print("Connected")
        else:
            print("Disconnected")

main()