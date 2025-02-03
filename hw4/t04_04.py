# 4.4. На відрізку [1.6, 3] знайдіть корінь рівняння
# sin 𝑥 = 𝑥 / 3.

import math

def find_root():
    # f(x) = sin(x) - x/3
    def f(x):
        return math.sin(x) - x / 3
    
    left, right = 1.6, 3.0  
    eps = 1e-7  
    
    while right - left > eps:
        mid = (left + right) / 2 
        if f(mid) * f(left) <= 0:
            right = mid  # шукаю у лівій частині
        else:
            left = mid  # у правій частині
    
    return left  # повертаю знайдений корінь

print(f"{find_root():.6f}")