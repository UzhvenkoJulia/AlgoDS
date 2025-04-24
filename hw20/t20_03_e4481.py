# Дерево відрізків.
# Завдання для самостійної роботи
# 20.3. У країні невивчених уроків (70%)
# Вказівка. У кожному завданні має бути побудоване та використане дерево відрізків.

'''import sys
import math

sys.setrecursionlimit(200000)

def build(node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start + end) // 2
        # піддерево
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = math.gcd(tree[2 * node], tree[2 * node +1])

def update(node, start, end, idx, val):
    if start == end:
        a[idx] = val
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            # у ліве піддерево
            update(2 * node, start, mid, idx, val)
        else:
            # у праве піддерево
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = math.gcd(tree[2 * node], tree[2 * node + 1])

# [l, r]
def query(node, start, end, l, r):
    if r < start or end < l:
        # не перетинаються — нейтральний елемент для НСД
        return 0
    if l <= start and end <= r:
        # входить у запит — поверт значення вузла
        return tree[node]
    # об'єд відповіді
    mid = (start + end) // 2
    left_gcd = query(2 * node, start, mid, l, r)
    right_gcd = query(2 * node + 1, mid + 1, end, l, r)
    return math.gcd(left_gcd, right_gcd)

n = int(input())                      
a = list(map(int, input().split()))  
m = int(input())                      

# дерево розміром 4n (з запасом)
tree = [0] * (4 * n)

build(1, 0, n - 1)

for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        # НСД — потрібно зменш індекси на 1 (бо індексація з 0)
        print(query(1, 0, n - 1, l - 1, r - 1))
    elif q == 2:
        # оновлення елемента у позиції l на значення r
        update(1, 0, n - 1, l - 1, r)'''


def gcd(x, y):
    while y != 0:
        x, y = y, x % y
    return x

def build(node, start, end):
    if start == end:
        tree[node] = a[start]
    else:
        mid = (start + end) // 2
        build(2 * node, start, mid)
        build(2 * node + 1, mid + 1, end)
        tree[node] = gcd(tree[2 * node], tree[2 * node + 1])

def update(node, start, end, idx, val):
    if start == end:
        a[idx] = val
        tree[node] = val
    else:
        mid = (start + end) // 2
        if start <= idx <= mid:
            update(2 * node, start, mid, idx, val)
        else:
            update(2 * node + 1, mid + 1, end, idx, val)
        tree[node] = gcd(tree[2 * node], tree[2 * node + 1])

# [l, r]
def query(node, start, end, l, r):
    if r < start or end < l:
        return 0  # нейтральний елемент для НСД
    if l <= start and end <= r:
        return tree[node]
    mid = (start + end) // 2
    left_gcd = query(2 * node, start, mid, l, r)
    right_gcd = query(2 * node + 1, mid + 1, end, l, r)
    return gcd(left_gcd, right_gcd)

n = int(input())                       
a = list(map(int, input().split()))   
m = int(input())                       

# 4n
tree = [0] * (4 * n)

build(1, 0, n - 1)

for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        # [l, r]
        print(query(1, 0, n - 1, l - 1, r - 1))
    elif q == 2:
        # l на r
        update(1, 0, n - 1, l - 1, r)