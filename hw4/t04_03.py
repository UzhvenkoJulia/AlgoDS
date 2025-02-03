# 4.3. Знайдіть найменше 𝑥 ∈ [0, 10], що
# 𝑓(𝑥) = 𝑥³ + 𝑥 + 1 > 5.

def find_min_x():
    # f(x) = x^3 + x + 1
    def f(x):
        return x**3 + x + 1
    
    left, right = 0.0, 10.0  
    eps = 1e-7  
    
    while right - left > eps:
        mid = (left + right) / 2 
        if f(mid) > 5:
            right = mid  # шукаємо у лівій частині
        else:
            left = mid  # у правій частині
    
    return left  # повертаємо найменше x, що задовольняє умову

print(f"{find_min_x():.6f}")