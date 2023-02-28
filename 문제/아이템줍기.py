#아이템줍기
from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    field = [[-1] * 102 for _ in range(102)]
    for rec in rectangle:
        x1, y1, x2, y2 = map(lambda x: x * 2, rec)
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if x1 < i < x2 and y1 < j < y2:
                    field[i][j] = 0
                elif field[i][j] != 0:
                    field[i][j] = 1
    q = deque()
    q.append([characterX * 2, characterY * 2])
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited = [[0] * 102 for _ in range(102)]
    visited[characterX*2][characterY*2] = 1
    while q:
        x, y = q.popleft()
        if x == itemX * 2 and y == itemY * 2:
            answer = visited[x][y] // 2
            break
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if visited[nx][ny] == 0 and field[nx][ny] == 1:
                q.append([nx, ny])
                visited[nx][ny] = visited[x][y] + 1
    return answer
