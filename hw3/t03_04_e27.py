original_number = int(input())
binary_digits = []

# перетворення числа у двійковий список
temp_number = original_number
while temp_number > 0:
    binary_digits.insert(0, temp_number % 2)
    temp_number //= 2

max_result = original_number 
shifts_made = 0               # к-сть виконаних циклічних зсувів

# циклічний зсув і перевірка max значення
while shifts_made < len(binary_digits):
    # зсув: беремо перший елемент і додаємо його в кінець
    first_bit = binary_digits.pop(0)
    binary_digits.append(first_bit)

    # обчисл десяткове значення нового двійкового числа
    new_number = 0
    for i, bit in enumerate(binary_digits):
        new_number += bit * (2 ** (len(binary_digits) - 1 - i))

    # оновлюємо max значення, якщо знайдене число більше
    if new_number > max_result:
        max_result = new_number

    shifts_made += 1  

print(max_result)