def selection_sort(arr):
    n = len(arr)  
    
    for i in range(n - 1):
        min_index = i  # припускаю, що мінімальний елемент знаходиться на позиції i
        
        # шукаємо найменший елемент у невідсортованій частині списку
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:  # якщо знайдено менший елемент
                min_index = j  # оновлюємо індекс мінімального елемента
        
        # якщо знайдений мінімальний елемент не на своєму місці, міняємо його місцями
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr  

n = int(input())  
words = [input().strip() for _ in range(n)]  # зчитуємо список слів

# сортування вибором
sorted_words = selection_sort(words)

for word in sorted_words:
    print(word)