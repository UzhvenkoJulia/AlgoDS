from matplotlib.pylab import f
from prometheus_client import g


def h(n):
    return f(n) + g(n)

# f(n) - 2.10, g(n) - 2.11

# розв'язок задачі 2.12
# функція h(n) визначена як сума функцій f(n) та g(n)


def f(n):
    # функція обчислює суму чисел від 1 до n
    # асимптотична оцінка: O(n)
    sum = 0
    for i in range(1, n + 1):  # f(n) = n(n+1) \ 2
        sum += i
    return sum

def g(n):
    # функція додає значення f(i) для всіх i від 1 до n
    # асимптотична оцінка: O(n^2)
    sum = 0
    for i in range(1, n + 1):  # O(1)
        sum += i + f(i)  # O(i)
        # O(1) + O(2) + O(3) + ... + O(n) = O (n(n+1) \ 2) = O(n^2)
    return sum

def h(n):
    # функція h(n) визначається як сума f(n) і g(n)
    # асимптотична оцінка: O(n^2)
    return f(n) + g(n)

# часова складність h(n) визначається найбільшим компонентом - O(n^2)
# O(h(n)) = O(n^2)

# аналіз асимптотичної складності функції h(n):
# f(n) має складність O(n), а g(n) має складність O(n^2)
# таким чином, h(n) = O(n^2)

# оптимізація: можна спростити обчислення суми для f(n) і g(n),
# використовуючи аналітичні формули для суми арифметичної прогресії

# ??
def optimized_f(n):
    return n * (n + 1) // 2  # -> O(1)

def optimized_g(n):
    sum = 0
    for i in range(1, n + 1):
        sum += i + optimized_f(i)
    return sum

#def g(n):
    #return sum(i + i * (i + 1) // 2 for i in range(1, n + 1))  # O(1)

def optimized_h(n):
    return optimized_f(n) + optimized_g(n)

# якщо у нас f(n) = O(1) та g(n) = O(1), то h(n) = O(1) виходить також таким же

# -> O(1)

def h(n):
    sum = (n + 1)*n // 2 + (n**3 + 6*n**2 + 5*n) // 6
    return sum  # O(1)