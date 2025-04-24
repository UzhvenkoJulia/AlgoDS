n, m = map(int, input().split()) 

degrees = [0] * n  

for _ in range(m):
    u, v = map(int, input().split())  
    degrees[u - 1] += 1 
    degrees[v - 1] += 1 

for degree in degrees:
    print(degree)