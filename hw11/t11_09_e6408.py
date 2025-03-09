# Зауваження. В задачі використовується дійсне ділення.


# перевірка чи можна отримати 24 за допомогою операцій
def can_get_24(nums):
    if len(nums) == 1:
        # якщо залишилось одне число, перевіряємо чи це 24
        return abs(nums[0] - 24) < 1e-6  # +точність для порівняння з дійсними числами

    for i in range(len(nums)):
        for j in range(len(nums)):
            if i != j:
                # створюємо новий список чисел, що включає все, крім nums[i] і nums[j]
                new_nums = [nums[k] for k in range(len(nums)) if k != i and k != j]
                
                for op in ['+', '-', '*', '/']:
                    if op == '+':
                        result = nums[i] + nums[j]
                    elif op == '-':
                        result = nums[i] - nums[j]
                    elif op == '*':
                        result = nums[i] * nums[j]
                    elif op == '/':
                        if nums[j] == 0:
                            continue
                        result = nums[i] / nums[j]
                    
                    # рекурсивно викликаємо функцію для нової підмножини чисел
                    if can_get_24(new_nums + [result]):
                        return True
    return False

# генерація перестановок чисел вручну
def generate_permutations(nums):
    if len(nums) == 1:
        return [nums]
    result = []
    for i in range(len(nums)):
        num = nums[i]
        remaining_nums = nums[:i] + nums[i+1:]
        for perm in generate_permutations(remaining_nums):
            result.append([num] + perm)
    return result

def main():
    t = int(input()) 
    for _ in range(t):
        # вхід: чотири числа для кожного тесту
        nums = list(map(int, input().split()))
        
        # генеруємо всі перестановки чисел вручну
        perms = generate_permutations(nums)
        
        # перевіряємо кожну перестановку
        found = False
        for perm in perms:
            if can_get_24(perm):
                found = True
                break
        
        if found:
            print("YES")
        else:
            print("NO")

main()