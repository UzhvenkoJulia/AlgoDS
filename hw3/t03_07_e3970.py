# Вказівка: Використайте бінарний пошук для знаходження відповіді для кожного вказаного інтервалу.

import sys

# читання всіх вхідних даних за один раз
input = sys.stdin.read
data = input().split()

# кількість звіряток
n = int(data[0])

# список кольорів звіряток (якщо є звірятка)
colors = list(map(int, data[1:n+1])) if n > 0 else []

# кількість запитів
m = int(data[n+1])

# список запитів
queries = list(map(int, data[n+2:n+2+m]))

# бінарний пошук першої позиції елемента, що не менший за target
def binary_search_left(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

# бінарний пошук першої позиції елемента, що більший за target
def binary_search_right(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low

# для кожного запиту виводимо кількість звіряток з заданим кольором
for query in queries:
    # знаходимо першу та останню позицію елемента, що рівний запиту
    left = binary_search_left(colors, query)
    right = binary_search_right(colors, query)
    
    # кількість елементів з кольором query
    print(right - left)


"""
# кількість звіряток
n = int(input())  

# якщо n більше 0, то читати список кольорів
if n > 0:
    colors = list(map(int, input().split()))
else:
    colors = []

# залежно від наявності даних, читати наступні значення
if n == 0:
    # переміщення до наступного рядка, який містить m
    input()
    
# кількість запитів
m = int(input())  

# список запитів
queries = list(map(int, input().split()))  # читання запитів

# не менший за target
def binary_search_left(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] < target:
            low = mid + 1
        else:
            high = mid
    return low

# більший за target
def binary_search_right(arr, target):
    low, high = 0, len(arr)
    while low < high:
        mid = (low + high) // 2
        if arr[mid] <= target:
            low = mid + 1
        else:
            high = mid
    return low

# для кожного запиту виводимо кількість звіряток з заданим кольором
for query in queries:
    # знаходимо першу та останню позицію елемента, що рівний запиту
    left = binary_search_left(colors, query)
    right = binary_search_right(colors, query)
    
    # кількість елементів з кольором query
    print(right - left)"""