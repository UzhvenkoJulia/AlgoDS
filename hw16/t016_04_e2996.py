# Дерева. Алгоритми на деревах.
# 16.4. Корупція (100%)
# Вказівка 1. У кожному завданні має бути реалізоване та використане дерево.
# Вказівка 2. Дерево має бути реалізоване як рекурсивна структура.

# представлення чиновника як вузла дерева
class Official:
    def __init__(self, bribe, subordinates):
        self.bribe = bribe                # сума хабара для цього чиновника
        self.subordinates = subordinates  # список підлеглих (номери чиновників)

# знаходження мін хабара, щоб отримати підпис міністра
def min_total_bribe(officials, current_id):
    current = officials[current_id]  # отрим поточного чиновника за його ID

    # якщо у чиновника немає підлеглих, йому можна одразу дати хабар
    if not current.subordinates:
        return current.bribe

    # мін хабар для всіх підлеглих
    subordinates_bribes = [min_total_bribe(officials, sub_id) for sub_id in current.subordinates]

    # щоб отримати підпис цього чиновника, спочатку треба підпис одного з підлеглих
    # отже, беру найменш хабар серед підлеглих і + хабар поточному
    return min(subordinates_bribes) + current.bribe

N = int(input()) 

officials = {}  # словник для зберігання всіх чиновників за їхніми номерами (ID)

for i in range(1, N + 1):
    parts = list(map(int, input().split()))
    bribe = parts[0]             # хабар цього чиновника
    k = parts[1]                 # к-сть підлеглих
    subordinates = parts[2:]     # список підлеглих
    officials[i] = Official(bribe, subordinates)  # + чиновника до словника

# починаючи з міністра (номер 1)
result = min_total_bribe(officials, 1)

print(result)