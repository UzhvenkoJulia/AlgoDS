# Дерева. Алгоритми на деревах.
# 16.7. Спільний предок – 2 (42%)
# Вказівка 1. У кожному завданні має бути реалізоване та використане дерево.
# Вказівка 2. Дерево має бути реалізоване як рекурсивна структура.

import sys
import threading  # щоб збільшити допустиму глибину рекурсії
# у задачі використовується глибока рекурсія (через dfs())

# обгортка потоку для уникнення обмежень Python на рекурсію
def main():
    import sys
    sys.setrecursionlimit(1 << 25)

    n, m = map(int, sys.stdin.readline().split())

    # зчит батьків для вершин 1...n-1 (корінь – вершина 0)
    parents = list(map(int, sys.stdin.readline().split()))

    # побудова дерева як списку нащадків для кожної вершини
    tree = [[] for _ in range(n)]

    for child in range(1, n):
        parent = parents[child - 1]
        tree[parent].append(child)

    # binary lifting
    LOG = 17  # тому що 2^17 > 1e5
    up = [[-1] * LOG for _ in range(n)]  # up[v][i] – 2^i-й предок вершини v
    depth = [0] * n  # глибина кожної вершини

    # рекурсивний обхід дерева для заповнення up[] і depth[]
    def dfs(v, p):

        up[v][0] = p

        for i in range(1, LOG):
            if up[v][i - 1] != -1:
                up[v][i] = up[up[v][i - 1]][i - 1]
        for to in tree[v]:
            depth[to] = depth[v] + 1
            dfs(to, v)

    # обхід з кореня (0)
    dfs(0, -1)

    # знаходження LCA (найменшого спільного предка)
    def lca(u, v):
        if depth[u] < depth[v]:
            u, v = v, u
        # переходжу, up to u на рівень v
        for i in reversed(range(LOG)):
            if up[u][i] != -1 and depth[up[u][i]] >= depth[v]:
                u = up[u][i]
        if u == v:
            return u
        # піднім u і v поки вони не стануть сусідами
        for i in reversed(range(LOG)):
            if up[u][i] != -1 and up[u][i] != up[v][i]:
                u = up[u][i]
                v = up[v][i]
        return up[u][0]

    a1, a2 = map(int, sys.stdin.readline().split())
    x, y, z = map(int, sys.stdin.readline().split())

    total = 0

    a_prev2 = a1
    a_prev1 = a2

    # перший запит
    v = lca(a1, a2)
    total += v

    for i in range(1, m):
        # a[2i-1], a[2i]
        a_i_1 = (x * a_prev2 + y * a_prev1 + z) % n
        a_i_2 = (x * a_prev1 + y * a_i_1 + z) % n

        # модифік першу вершину з урахуванням попередньої відповіді
        u = (a_i_1 + v) % n
        w = a_i_2

        v = lca(u, w)
        total += v

        a_prev2, a_prev1 = a_i_1, a_i_2

    print(total)

threading.Thread(target=main).start()