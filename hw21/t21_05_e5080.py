n = int(input())  
graph = []  

for _ in range(n):
    row = list(map(int, input().split()))  
    graph.append(row)  

hanging_vertices = 0  

for i in range(n):
    degree = sum(graph[i])  # степінь вершини i (сума елем в i-му рядку матриці)
    if degree == 1:  
        hanging_vertices += 1 

print(hanging_vertices)