# Сортування
# Сортування – швидкі алгоритми
# Використайте алгоритм швидкого сортування (без надмірного використання додаткової пам'яті)

def quicksort(arr, low, high):
    while low < high:
        pivot_index = partition(arr, low, high)  # знаходимо точку розбиття
        if pivot_index - low < high - pivot_index:
            quicksort(arr, low, pivot_index - 1)  # рекурсивно сортуємо ліву частину
            low = pivot_index + 1  # переходимо до правої частини
        else:
            quicksort(arr, pivot_index + 1, high)  # рекурсивно сортуємо праву частину
            high = pivot_index - 1  # переходимо до лівої частини

def partition(arr, low, high):
    mid = (low + high) // 2  # обираємо середній елемент як pivot
    arr[mid], arr[high] = arr[high], arr[mid]  # переміщуємо pivot в кінець
    pivot = arr[high]  # опорний елемент
    i = low - 1  # індекс для розміщення елементів, менших за pivot
    
    for j in range(low, high):
        if arr[j] <= pivot:  # якщо поточний елемент менший або рівний pivot
            i += 1  # зсуваємо межу меншої частини
            arr[i], arr[j] = arr[j], arr[i]  
    
    arr[i + 1], arr[high] = arr[high], arr[i + 1]  # ставимо pivot на правильне місце
    return i + 1  # повертаємо новий індекс pivot

n = int(input())  
arr = list(map(int, input().split()))  # масив чисел

quicksort(arr, 0, n - 1)

print(" ".join(map(str, arr)))
