# 4.5. На відрізку [0, 2] знайдіть корінь рівняння
# 𝑥³ + 4𝑥² + 𝑥 − 6 = 0.

def find_root():
    # f(x) = x^3 + 4x^2 + x - 6
    def f(x):
        return x**3 + 4*x**2 + x - 6
    
    left, right = 0.0, 2.0 
    eps = 1e-7 
    
    while right - left > eps:
        mid = (left + right) / 2  
        if f(mid) * f(left) <= 0:
            right = mid  
        else:
            left = mid  
    
    return left  

print(f"{find_root():.6f}")