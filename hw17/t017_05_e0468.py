# Бінарні дерева. Бінарні дерева пошуку.
# Завдання для самостійної роботи
# 17.5. Дерево (50%)
# Вказівка 1. У кожному завданні має бути реалізоване та використане бінарне дерево.
# Вказівка 2. Дерево має бути реалізоване як рекурсивна структура.


# перевірити, чи може задана послідовність бути шляхом у бінарному дереві пошуку
# рекурсивна реалізація, де кожен вузол дерева представлений класом

import sys


# усув зайві пробіли та символи переведення рядка
sequence = list(map(int, sys.stdin.read().split()))

class Node:
    def __init__(self, value):
        self.value = value  
        self.left = None    
        self.right = None   

# вставка елем 
def insert(node, value):
    # дерево порожнє - створ новий вузол
    if node is None:
        return Node(value)
    if value < node.value:
        node.left = insert(node.left, value)
    elif value > node.value:
        node.right = insert(node.right, value)
    return node  

# перевірка, чи може послідовність бути шляхом
def is_valid_bst_path(seq):
    # дерево порожнє — шлях можливий лише якщо немає елементів
    if not seq:
        return True

    # перш елем як кореня
    root = Node(seq[0])

    # поточний вузол дерева, йдемо по шляху
    current = root

    min_val = float('-inf')
    max_val = float('inf')

    for value in seq[1:]:
        if value < current.value:
            # якщо ліве піддерево існує і значення більше або рівне, то шлях -
            if current.left:
                current = current.left
                if not (value < current.value):
                    return False
            else:
                current.left = Node(value)
                current = current.left
        elif value > current.value:
            # якщо праве піддерево існує і значення менше або рівне, то шлях -
            if current.right:
                current = current.right
                if not (value > current.value):
                    return False
            else:
                # переходимо до вузла, після його вставки
                current.right = Node(value)
                current = current.right
        else:
            # значення не можуть повторюватися
            return False

    return True

if is_valid_bst_path(sequence):
    print("YES")
else:
    print("NO")


'''
import sys

# числа розділені пробілами або переносами рядка
sequence = list(map(int, sys.stdin.read().split()))

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def is_valid_bst_path(seq):
    if not seq:
        return True

    root = Node(seq[0])

    current = root
    min_val = float('-inf')
    max_val = float('inf')

    for value in seq[1:]:
        # якщо значення не в допустимих межах — порушення правил 
        if not (min_val < value < max_val):
            return False

        if value < current.value:
            # -> вліво: верхня межа зменшується
            if current.left is None:
                current.left = Node(value)
                current = current.left
                max_val = current.value 
            else:
                current = current.left
                max_val = current.value
        elif value > current.value:
            # -> вправо: нижня межа зростає
            if current.right is None:
                current.right = Node(value)
                current = current.right
                min_val = current.value  
            else:
                current = current.right
                min_val = current.value
        else:
            # повторювані значення заборонено
            return False

    return True

if is_valid_bst_path(sequence):
    print("YES")
else:
    print("NO")
'''