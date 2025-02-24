#  Сортування злиттям
# Використайте алгоритм сортування злиттям

def merge_sort(arr):
    if len(arr) > 1:
        mid = len(arr) // 2  
        left_half = arr[:mid]  
        right_half = arr[mid:]  

        merge_sort(left_half)  # рекурсивне сортування лівої частини
        merge_sort(right_half)  # правої частини

        # об'єднання відсортованих частин
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i][0] <= right_half[j][0]:  # порівнюємо основні номери
                arr[k] = left_half[i]
                i += 1
            else:
                arr[k] = right_half[j]
                j += 1
            k += 1

        # додаємо залишки елементів, якщо вони є
        while i < len(left_half):
            arr[k] = left_half[i]
            i += 1
            k += 1

        while j < len(right_half):
            arr[k] = right_half[j]
            j += 1
            k += 1

n = int(input()) 
robots = [tuple(map(int, input().split())) for _ in range(n)]  
# tuple (кортеж)

merge_sort(robots)  

for robot in robots:
    print(robot[0], robot[1])
# основний номер і допоміжний номер робота