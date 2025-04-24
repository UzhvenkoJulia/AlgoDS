n, m = map(int, input().split()) 

in_degrees = [0] * n  # півстеп входу для кожної вершини
out_degrees = [0] * n  

for _ in range(m):
    u, v = map(int, input().split()) 
    out_degrees[u - 1] += 1 
    in_degrees[v - 1] += 1  

for i in range(n):
    print(in_degrees[i], out_degrees[i])