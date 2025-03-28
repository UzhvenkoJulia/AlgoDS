# 13.5. Дужкова послідовність (100%)

def is_valid_bracket_sequence(s: str) -> str:
    stack = []  
    bracket_map = {')': '(', ']': '[', '}': '{'}  # відповідності закриваючих дужок
    
    for char in s:
        if char in bracket_map.values():  # якщо відкриваюча дужка
            stack.append(char)
        elif char in bracket_map:  # якщо закриваюча дужка
            if not stack or stack.pop() != bracket_map[char]:
                return "no"
    
    return "yes" if not stack else "no"

s = input().strip()

print(is_valid_bracket_sequence(s))