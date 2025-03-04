# 10.5. CD (100%)

import sys  # для читання вхідних даних

def find_best_sum(N, tracks):
    dp = [0] * (N + 1)  # dp[i] — максимальна сума, яку можна набрати до i хвилин
    # динамічне програмування
    # касета довжиною N
    # [0] * (N + 1) – створює масив із N + 1 елементів, заповнених нулями
    # спочатку жодна хвилина не зайнята, будемо поступово оновлювати масив

    for track in tracks:
        for j in range(N, track - 1, -1):  # заповнюємо у зворотному порядку
            dp[j] = max(dp[j], dp[j - track] + track)

    return dp[N]  # максимальна можлива сума

def process_input():
    for line in sys.stdin:
        data = list(map(int, line.split()))
        N = data[0]  # максимальний час запису
        tracks = data[2:]  # довжини треків
        # з третього елемента

        best_sum = find_best_sum(N, tracks)  

        print(f"sum:{best_sum}") 

process_input()