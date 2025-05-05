import sys

input = sys.stdin.readline

from collections import deque

def solve(n, m, grid):
    visited = [[False] * m for _ in range(n)]
    directions = [(-1,0), (1,0), (0,-1), (0,1)]  

    queue = deque()
    queue.append((0, 0, 0))  # (x, y, number_of_tilts)
    visited[0][0] = True

    while queue:
        x, y, steps = queue.popleft()

        for dx, dy in directions:
            nx, ny = x, y

            # рух поки не попаду в 1 або межу
            while True:
                tx, ty = nx + dx, ny + dy
                if not (0 <= tx < n and 0 <= ty < m) or grid[tx][ty] == 1:
                    break
                nx, ny = tx, ty
                if grid[nx][ny] == 2:
                    return steps + 1  # провалася в отвір

            # +якщо ще не відвідано і це не стартова позиція
            if not visited[nx][ny]:
                visited[nx][ny] = True
                queue.append((nx, ny, steps + 1))

    return -1  # вихід існує

if __name__ == '__main__':
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]
    
    print(solve(n, m, grid))