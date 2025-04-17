# Двійкова купа та пріоритетна черга.
# Зауваження. Вимоги до алгоритму виконання задачі відсутні.
# 19.3. Куча чи ні? (100%)

# масив - двійкова купа (мін-кучею)
def is_heap(arr):
    n = len(arr)  

    # ітер по всіх внутрішніх вузлах дерева, тобто з 0 до (n-2)//2 включно
    for i in range((n - 2) // 2 + 1):
        left = 2 * i + 1      
        right = 2 * i + 2     

        # чи лівий нащадок існує та чи не порушує властивість купи
        if left < n and arr[i] > arr[left]:
            return False  # якщо поточний елемент більший за лівого нащадка, то це не купа

        if right < n and arr[i] > arr[right]:
            return False  

    # масив є купою - перевірки +
    return True


n = int(input())  
arr = list(map(int, input().split())) 

if is_heap(arr):
    print("YES")
else:
    print("NO")