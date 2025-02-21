def insertion_sort(arr):
    n = len(arr)  
    
    # починаючи з другого
    for i in range(1, n):
        key = arr[i]  # поточний елемент, який будемо вставляти
        j = i - 1
        
        # переміщуємо елементи, які більші за key, на одну позицію вперед
        while j >= 0 and (arr[j] % 10 > key % 10 or (arr[j] % 10 == key % 10 and arr[j] > key)):
            # якщо остання цифра arr[j] більша за останню цифру key, то arr[j] має бути переміщене вправо
            # arr[j + 1] = arr[j]
            # переміщуємо arr[j] вправо, щоб звільнити місце для вставки key
            arr[j + 1] = arr[j]
            j -= 1
            # зменшуємо j, щоб перевірити попередній елемент
        
        arr[j + 1] = key  # вставляємо key на правильну позицію
    
    return arr 

n = int(input())  
numbers = [int(input().strip()) for _ in range(n)]  # список чисел

# сортування вставкою
sorted_numbers = insertion_sort(numbers)

print(" ".join(map(str, sorted_numbers)))