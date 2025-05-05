import sys
sys.setrecursionlimit(200000)


input = sys.stdin.readline

def main():
    N, M = map(int, input().split())

    graph = [[] for _ in range(N + 1)]

    for _ in range(M):
        u, v = map(int, input().split())
        graph[u].append(v)
        graph[v].append(u)

    visited = [False] * (N + 1)
    components = []

    def dfs(start):
        stack = [start]
        comp = []
        
        while stack:
            node = stack.pop()
            if not visited[node]:
                visited[node] = True
                comp.append(node)
                for neighbor in graph[node]:
                    if not visited[neighbor]:
                        stack.append(neighbor)
        return comp

    for i in range(1, N + 1):
        if not visited[i]:
            comp = dfs(i)
            components.append(comp)

    print(len(components))
    for comp in components:
        print(len(comp))
        print(' '.join(map(str, comp)))

main()