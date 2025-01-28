# Використайте лінійний пошук для підрахунку відповіді.

def process_queries(input_data):
    lines = input_data.strip().split("\n")
    # strip() видаляє всі пробіли, символи нового рядка (\n) та табуляції (\t) з початку та кінця рядка
    # split("\n") розділяє рядок input_data на частини за символом нового рядка (\n)
    results = []
    i = 0

    while i < len(lines):
        # к-сть членів делегації
        n = int(lines[i])
        i += 1

        heights = list(map(int, lines[i].split()))
        i += 1

        a, b = map(int, lines[i].split())
        # map() застосовує передану функцію (int) до кожного елемента списку, отриманого після split()
        i += 1

        # лінійний підрахунок кількості членів у межах [a, b]
        count = 0
        for h in heights:
            if a <= h <= b:
                count += 1

        results.append(count)

    # повернення результату для кожного запиту
    return "\n".join(map(str, results))


if __name__ == "__main__":
    import sys
    input_data = sys.stdin.read()
    output = process_queries(input_data)
    print(output)