# Дійсний бінарний пошук

import sys

def find_x(C):
    # x не може бути меншим за 0
    left, right = 0.0, C
    
    eps = 1e-7
    
    while right - left > eps:
        mid = (left + right) / 2  
        
        # значення функції у точці mid
        f_mid = mid ** 2 + mid ** 0.5
        
        if abs(f_mid - C) < eps:
            return mid  
        
        if f_mid < C:
            left = mid  # розв'язок знаходиться у правій частині
        else:
            right = mid  # розв'язок знаходиться у лівій частині
    
    return (left + right) / 2  # наближене значення

if __name__ == "__main__":
    C = float(sys.stdin.readline().strip())
    
    result = find_x(C)
    
    print(f"{result:.6f}")