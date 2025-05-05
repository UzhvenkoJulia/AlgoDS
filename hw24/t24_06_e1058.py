import sys
sys.setrecursionlimit(10000)  

directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def dfs(grid, x, y, N, M):
    # поточна клітинка - відвідана
    grid[x][y] = False  # False, щоб позначити, що клітинка вже відвідана
    size = 1  
    
    for dx, dy in directions:
        nx, ny = x + dx, y + dy
        if 0 <= nx < N and 0 <= ny < M and grid[nx][ny]:
            size += dfs(grid, nx, ny, N, M)
    
    return size

def main():
    N, M, K = map(int, input().split())
    
    grid = [[False] * M for _ in range(N)]
    
    for _ in range(K):
        r, c = map(int, input().split())
        grid[r - 1][c - 1] = True  # індексація з 0
    
    max_lake_size = 0
    
    for i in range(N):
        for j in range(M):
            if grid[i][j]:  # якщо клітинка залита водою і не була відвідана
                lake_size = dfs(grid, i, j, N, M)
                max_lake_size = max(max_lake_size, lake_size)  
    
    print(max_lake_size)

main()