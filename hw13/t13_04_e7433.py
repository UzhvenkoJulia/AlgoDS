# Стек та його застосування.
# Завдання для самостійної роботи
# 13.4. Система числення (100%)
# Вказівка. У кожному завданні має бути використаний стек (реалізовувати не обов'язково).

from collections import deque


def convert_to_base(A: str, P: str) -> str:
    
    # у цілі числа
    A = int(A)
    P = int(P)
    
    # стек (deque) для зберігання залишків
    stack = deque()
    
    # перетворюємо число у нову систему числення
    while A > 0:
        remainder = A % P  # залишок від ділення на P
        stack.appendleft(remainder)  # + у стек зліва (імітація стеку)
        A //= P  # оновлюю A, ділячи націло на P
    
    result = "".join(f"[{x}]" if x > 9 else str(x) for x in stack)
    
    return result

A = input().strip()
P = input().strip()

print(convert_to_base(A, P))