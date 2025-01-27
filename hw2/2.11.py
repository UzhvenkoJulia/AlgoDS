# Оцінка асимптотичної складності функції g(n)
# f(n)

# 2.10
def f(n): 
    sum = 0
    for i in range(1, n + 1):  # f(n) = n(n+1) \ 2
        sum = sum + i
    return sum


from matplotlib.pylab import f


def g(n):
    sum = 0
    for i in range(1, n + 1):  # O(1)
        sum = sum + i + f(i)  # O(i)
        # O(1) + O(2) + O(3) + ... + O(n) = O (n(n+1) \ 2) = O(n^2)
    return sum

# пояснення:
# у функції g(n) виконується n ітерацій циклу for
# на кожній ітерації викликається функція f(i), яка має складність O(i)
# у найгіршому випадку це означає:
# f(1) + f(2) + f(3) + ... + f(n), тобто 1 + 2 + 3 + ... + n = n * (n + 1) // 2
# таким чином, складність функції g(n) дорівнює O(n^2)

# оптимізація функції g(n):
# використовуючи оптимізовану версію f(n), можна зменшити константи,
# але асимптотична складність залишиться O(n^2)

def optimized_g(n):
    sum = 0
    for i in range(1, n + 1):
        sum = sum + i + optimized_g(i)
        # sum = sum + i + optimized_f(i) ??
    return sum

def g(n):
    sum_f = sum(f(i) for i in range(1, n + 1))  # збираємо всі значення f(i) одночасно
    return sum(range(1, n + 1)) + sum_f

# можна оптимізувати до O(1):

def g(n):
    return (n * (n + 1)) // 2 + n * f(1)  # f(i) = f(1) = c для всіх i

def g(n):
    return (n * (n + 1)) // 2 + (n * (n + 1)) // 2  # Сума чисел від 1 до n двічі

# результатом виконання є сума вигляду:

def g(n, a, b):
    sum_i = (n * (n + 1)) // 2  # сума від 1 до n
    sum_f = a * sum_i + b * n  # сума f(i) для лінійної функції f(i) = ai + b
    return sum_i + sum_f

# n * (n + 1) \ 2 + n * (n + 1) \ 4 + n * ((n + 1)(2n + 1)) \ 12 = n^3 + 6n^2 + 5n \ 6

def g(n):
    sum = (n**3 + 6*n**2 + 5*n) // 6  # O(1)
    return sum  # O(1)