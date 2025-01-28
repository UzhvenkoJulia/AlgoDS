## 2 * 10^9
## 1 ≤ n ≤ 10^5
## 1 ≤ m ≤ 10^5

#import bisect  # для виконання бінарного пошуку

#n = int(input())  # к=сть видів метеликів у колекції
#collection = list(map(int, input().split()))  # упорядковані номери видів метеликів
#m = int(input())  # к-сть запитів
#queries = list(map(int, input().split()))  # номери видів, що запитуються

## для кожного запиту перевіряємо, чи є такий вид у колекції
#for query in queries:
#    # використовую бінарний пошук для перевірки наявності виду
#    index = bisect.bisect_left(collection, query)
#    if index < n and collection[index] == query:
#        print("YES")
#    else:
#        print("NO")

## bisect_left повертає індекс, де можна вставити елемент query в масив collection, щоб зберегти його відсортованим


def binary_search(arr, x):
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2  # середина масиву
        if arr[mid] == x:
            return True
        elif arr[mid] < x:
            left = mid + 1
        else:
            right = mid - 1
    return False

n = int(input())  # к-сть видів метеликів у колекції
collection = list(map(int, input().split()))  # упорядковані номери видів метеликів
m = int(input())  # к-сть запитів
queries = list(map(int, input().split()))  # номери видів, що запитуються

for query in queries:
    if binary_search(collection, query):
        print("YES")
    else:
        print("NO")