from collections import deque

def generate_moves(number):
    moves = []
    s = str(number)  

    # збільш першу цифру на 1 (якщо не 9)
    if s[0] != '9':
        new_first_digit = str(int(s[0]) + 1)
        moves.append(int(new_first_digit + s[1:]))

    # зменш останню цифру на 1 (якщо не 1)
    if s[-1] != '1':
        new_last_digit = str(int(s[-1]) - 1)
        moves.append(int(s[:-1] + new_last_digit))

    # циклічний зсув вправо
    moves.append(int(s[-1] + s[:-1]))

    # циклічний зсув вліво
    moves.append(int(s[1:] + s[0]))

    return moves

start = int(input())
end = int(input())

# поточне число, шлях до нього
queue = deque()
queue.append((start, [start]))

# множина відвіданих чисел, щоб не заходити двічі в одну вершину
visited = set()
visited.add(start)

while queue:
    current, path = queue.popleft()

    if current == end:
        for num in path:
            print(num)
        break

    for next_number in generate_moves(current):
        if next_number not in visited:
            visited.add(next_number)
            queue.append((next_number, path + [next_number]))