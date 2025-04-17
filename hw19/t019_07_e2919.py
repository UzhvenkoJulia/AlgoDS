# Двійкова купа та пріоритетна черга.
# 19.7. Це ліва куча?
# Вказівка. У кожному завданні має бути реалізована та використана бінарна купа

# потенціал — найкоротша відстань до вершини з менше ніж двома дітьми
# ліве дерево повинно задовольняти: 
# 1. потенціал лівого >= потенціалу правого
# 2. не може бути правого сина без лівого

import sys
sys.setrecursionlimit(200000)  

n = int(input())
tree = {}  # словник: номер вершини -> (лівий, правий)

# побудова дерева і визначення кореня
all_nodes = set(range(1, n+1))
children = set()

for i in range(1, n+1):
    l, r = map(int, input().split())
    tree[i] = (l, r)
    if l != -1:
        children.add(l)
    if r != -1:
        children.add(r)

# корінь - це вершина, яка не є жодним із дітей
roots = list(all_nodes - children)

root = roots[0] if roots else 1  # вибір, якщо кореня не знайдено

potential = {}

def compute_potential(node):
    if node == -1:
        return 0  # якщо немає вершини 
    if node in potential:
        return potential[node]
    
    left, right = tree[node]
    
    # якщо вершина має менше ніж 2 дітей — потенціал = 1
    if left == -1 or right == -1:
        potential[node] = 1
        return 1
    
    left_pot = compute_potential(left)
    right_pot = compute_potential(right)
    
    # потенціал — мінімум з потенціалів дітей + 1
    potential[node] = min(left_pot, right_pot) + 1
    return potential[node]

for node in range(1, n + 1):
    compute_potential(node)

# найменш за номером вершина, де порушується умова

def find_violation(node):
    if node == -1:
        return -1  # якщо порожній — порушення немає

    left, right = tree[node]

    # якщо правий є, а лівого немає — порушення
    if left == -1 and right != -1:
        return node
    
    # потенціал лівого < правого — порушення
    if left != -1 and right != -1:
        if potential[left] < potential[right]:
            return node
    
    left_check = find_violation(left)
    if left_check != -1:
        return left_check
    right_check = find_violation(right)
    return right_check

violation = find_violation(root)

print(violation)