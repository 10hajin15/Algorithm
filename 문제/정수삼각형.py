#정수 삼각형
n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(1, len(graph)):
    for j in range(len(graph[i])):
        if j == 0:
            graph[i][j] = graph[i-1][j] + graph[i][j]
        elif j == len(graph[i])-1:
            graph[i][j] = graph[i-1][j-1] + graph[i][j]
        else:
            graph[i][j] = max(graph[i-1][j-1], graph[i-1][j]) + graph[i][j]

print(max(graph[n-1]))

