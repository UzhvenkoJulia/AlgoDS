import sys
sys.setrecursionlimit(200000)  

def main():
    input = sys.stdin.readline

    n, m = map(int, input().split())
    adj = [[] for _ in range(n + 1)]
    for _ in range(m):
        u, v = map(int, input().split())
        adj[u].append(v)

    visited = [0] * (n + 1)  
    result = []
    has_cycle = [False]

    def dfs(u):
        visited[u] = 1
        for v in adj[u]:
            if visited[v] == 0:
                dfs(v)
                if has_cycle[0]:
                    return
            elif visited[v] == 1:
                has_cycle[0] = True
                return
        visited[u] = 2
        result.append(u)

    for u in range(1, n + 1):
        if visited[u] == 0:
            dfs(u)
            if has_cycle[0]:
                print(-1)
                return

    print(' '.join(map(str, reversed(result))))

main()