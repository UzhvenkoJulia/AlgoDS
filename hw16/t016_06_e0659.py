# Дерева. Алгоритми на деревах.
# 16.6. Дерево гри (100%)
# Вказівка 1. У кожному завданні має бути реалізоване та використане дерево.
# Вказівка 2. Дерево має бути реалізоване як рекурсивна структура.

class GameNode:
    def __init__(self, is_leaf, value=None):
        self.children = []       # для внутрішніх вузлів
        self.is_leaf = is_leaf   # чи є вузол листком?
        self.value = value       # значення результату гри (для листків)

    def evaluate(self, is_first_player):

        """
        рекурсивна функція оцінки стану гри
        is_first_player показує, хто зараз робить хід (True – перший гравець, False – другий)
        
        +1, якщо перший гравець гарантовано виграє;
        -1, якщо другий гравець гарантовано виграє;
         0, якщо буде нічия за оптимальної гри.
        """

        if self.is_leaf:
            return self.value  # якщо це листок, повертаємо його значення (+1, -1 або 0)

        # значення кожної дитини
        results = [child.evaluate(not is_first_player) for child in self.children]

        if is_first_player:
            return max(results)
        else:
            return min(results)  

n = int(input())  
nodes = [None] * (n + 1) 

# корінь (завжди внутрішній вузол)
nodes[1] = GameNode(is_leaf=False)

for i in range(2, n + 1):
    parts = input().split()
    type_node = parts[0]      # 'N' або 'L'
    parent = int(parts[1])    # номер батьківського вузла

    if type_node == 'L':
        result = int(parts[2])  # -1, 0 або +1
        nodes[i] = GameNode(is_leaf=True, value=result)
    else:
        nodes[i] = GameNode(is_leaf=False)

    # + вузол як нащадка до батька
    nodes[parent].children.append(nodes[i])

# результат гри, починаючи з кореня (гравець 1 ходить першим)
result = nodes[1].evaluate(is_first_player=True)

if result > 0:
    print("+1")
elif result < 0:
    print("-1")
else:
    print("0")