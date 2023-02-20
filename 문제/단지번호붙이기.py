#단지번호붙이기
from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int, input())))

result = []
def bfs(x, y):
    queue = deque()
    queue.append((x, y))
    graph[x][y] = 0
    count = 1
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= n:
                continue
            if graph[nx][ny] == 1:
                queue.append((nx, ny))
                graph[nx][ny] = 0
                count += 1
    result.append(count)

for i in range(n):
    for j in range(n):
        if graph[i][j] != 0:
            bfs(i, j)

print(len(result))
result.sort()
for i in result:
    print(i)