# співвідношення

def a(n):
    total = 0
    for i in range(n + 1):
        total += i
    return total

def b(n):
    total = 0
    for i in range(n + 1):
        total += i * i
    return total

def c(n, a):
    total = 1
    for i in range(n + 1):
        total += a
        a *= a
    return total

def d(n):
    total = 0
    for i in range(n + 1):
        powered = 1
        for j in range(i):
            powered *= i
        total += powered
    return total

def e(n):
    total = 1.0
    for i in range(1, n + 1):
        total *= 1.0 / (1 + i)
    return total

def f(n):
    total = 1.0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total *= 1.0 / (1 + fact)
    return total

def g(n, a):
    total = 1.0
    fact = 1
    for i in range(1, n + 1):
        fact *= i
        total *= float(a) / (1 + fact)
        a *= a
    return total

def h(n, m):
    total = 1.0
    for i in range(1, n + 1):
        powered = 1
        for j in range(m):
            powered *= i
        total *= 1.0 / (1 + powered)
    return total

def i(n, m):
    total = 1.0
    for i in range(1, n + 1):
        powered = 1
        for j in range(i):
            powered *= i
        total *= 1.0 / (1 + powered)
    return total
