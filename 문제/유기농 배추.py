#유기농 배추
#DFS
# import sys
# sys.setrecursionlimit(10000)
#
# for tc in range(int(input())):
#     n, m, k = map(int, input().split())
#     graph = [[0] * m for _ in range(n)]
#     for i in range(k):
#         a, b = map(int, input().split())
#         graph[a][b] = 1
#     def dfs(x, y):
#         if x < 0 or y < 0 or x >= n or y >= m:
#             return False
#         if graph[x][y] == 1:
#             graph[x][y] = 0
#             dfs(x - 1, y)
#             dfs(x + 1, y)
#             dfs(x, y - 1)
#             dfs(x, y + 1)
#             return True
#         return False
#     result = 0
#     for i in range(n):
#         for j in range(m):
#             if dfs(i, j) == True:
#                 result += 1
#     print(result)

#BFS
from collections import deque

#상하좌우
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    queue = deque()
    queue.append((x,y))
    graph[x][y] = 0
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= n or ny >= m:
                continue
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                queue.append((nx, ny))
    return

for tc in range(int(input())):
    m, n, k = map(int, input().split())
    graph = [[0] * m for _ in range(n)]
    for i in range(k):
        a, b = map(int, input().split())
        graph[b][a] = 1

    result = 0
    for i in range(m):
        for j in range(n):
            if graph[j][i] == 1:
                bfs(j, i)
                result += 1
    print(result)