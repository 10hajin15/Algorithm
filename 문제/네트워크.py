#네트워크
from collections import deque
def bfs(computers, x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for i in range(len(computers[x])):
            if computers[i][x] == 1:
                computers[x][y] = 0
                computers[y][x] = 0
                q.append((i, x))
def solution(n, computers):
    answer = 0
    for i in range(n):
        for j in range(len(computers[i])):
            if computers[i][j] == 1:
                bfs(computers, i, j)
                answer += 1
    return answer

print(solution(3, [[1, 1, 0], [1, 1, 1], [0, 1, 1]]	))