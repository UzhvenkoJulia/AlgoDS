# Дерево відрізків.
# Завдання для самостійної роботи
# 20.4. У країні невивчених уроків 2 (63%)
# Вказівка. У кожному завданні має бути побудоване та використане дерево відрізків.

def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def lcm(a, b):
    if a == 0 or b == 0:
        return 0
    return a // gcd(a, b) * b

def build_gcd(node, start, end):
    if start == end:
        gcd_tree[node] = a[start]
    else:
        mid = (start + end) // 2
        build_gcd(2 * node, start, mid)
        build_gcd(2 * node + 1, mid + 1, end)
        gcd_tree[node] = gcd(gcd_tree[2 * node], gcd_tree[2 * node + 1])

def build_lcm(node, start, end):
    if start == end:
        lcm_tree[node] = a[start]
    else:
        mid = (start + end) // 2
        build_lcm(2 * node, start, mid)
        build_lcm(2 * node + 1, mid + 1, end)
        lcm_tree[node] = lcm(lcm_tree[2 * node], lcm_tree[2 * node + 1])

def query_gcd(node, start, end, l, r):
    if r < start or end < l:
        return 0  
    if l <= start and end <= r:
        return gcd_tree[node]
    mid = (start + end) // 2
    left = query_gcd(2 * node, start, mid, l, r)
    right = query_gcd(2 * node + 1, mid + 1, end, l, r)
    return gcd(left, right)

def query_lcm(node, start, end, l, r):
    if r < start or end < l:
        return 1 
    if l <= start and end <= r:
        return lcm_tree[node]
    mid = (start + end) // 2
    left = query_lcm(2 * node, start, mid, l, r)
    right = query_lcm(2 * node + 1, mid + 1, end, l, r)
    return lcm(left, right)

def update_gcd(node, start, end, idx, val):
    if start == end:
        gcd_tree[node] = val
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update_gcd(2 * node, start, mid, idx, val)
        else:
            update_gcd(2 * node + 1, mid + 1, end, idx, val)
        gcd_tree[node] = gcd(gcd_tree[2 * node], gcd_tree[2 * node + 1])

def update_lcm(node, start, end, idx, val):
    if start == end:
        lcm_tree[node] = val
    else:
        mid = (start + end) // 2
        if idx <= mid:
            update_lcm(2 * node, start, mid, idx, val)
        else:
            update_lcm(2 * node + 1, mid + 1, end, idx, val)
        lcm_tree[node] = lcm(lcm_tree[2 * node], lcm_tree[2 * node + 1])

n = int(input())                      
a = list(map(int, input().split()))  
m = int(input())                     

gcd_tree = [0] * (4 * n)
lcm_tree = [1] * (4 * n)  

build_gcd(1, 0, n - 1)
build_lcm(1, 0, n - 1)

for _ in range(m):
    q, l, r = map(int, input().split())
    if q == 1:
        left = l - 1
        right = r - 1
        gcd_val = query_gcd(1, 0, n - 1, left, right)
        lcm_val = query_lcm(1, 0, n - 1, left, right)
        if gcd_val < lcm_val:
            print("wins")
        elif gcd_val > lcm_val:
            print("loser")
        else:
            print("draw")
    elif q == 2:
        # a[l] = r
        idx = l - 1
        a[idx] = r
        update_gcd(1, 0, n - 1, idx, r)
        update_lcm(1, 0, n - 1, idx, r)