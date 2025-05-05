from collections import deque

NOT_CUT = "#"   
CUT_OUT = "." 

VISITED = 1     
EMPTY = 0       

DIRECTIONS = ((0, -1), (-1, 0), (0, 1), (1, 0))


def solve(maze, m, n):
    """
    повертає к-сть зв'язних компонент 

    maze — список списків з символами '#' та '.'
    """
    visited = [
        [EMPTY for _ in range(n)] 
        for _ in range(m)
    ]

    count = 0  

    for i in range(m):
        for j in range(n):
            if maze[i][j] == NOT_CUT and visited[i][j] == EMPTY:
                queue = deque()
                queue.append((i, j))
                visited[i][j] = VISITED  

                while queue:
                    ci, cj = queue.popleft()
                    for di, dj in DIRECTIONS:
                        ni = ci + di
                        nj = cj + dj
                        if 0 <= ni < m and 0 <= nj < n:
                            # якщо сусідня клітинка не вирізана і не відвідана
                            if maze[ni][nj] == NOT_CUT and visited[ni][nj] == EMPTY:
                                visited[ni][nj] = VISITED 
                                queue.append((ni, nj))   
                count += 1
    return count

if __name__ == '__main__':

    m, n = map(int, input().split())  
    maze = [list(input().strip()) for _ in range(m)] 

    print(solve(maze, m, n))