#게임 맵 최단거리
from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(maps, x, y):
    visited = [[False] * len(maps[0]) for _ in range(len(maps))]
    queue = deque()
    queue.append((x,y))
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or ny < 0 or nx >= len(maps) or ny >= len(maps[0]):
                continue
            if maps[nx][ny] == 0: continue
            if maps[nx][ny] == 1 and visited[nx][ny] == False:
                maps[nx][ny] = maps[x][y] + 1
                queue.append((nx, ny))
                visited[nx][ny] = True
    if maps[-1][-1] == 1: return -1
    return maps[-1][-1]

def solution(maps):
    return bfs(maps, 0, 0)

print(solution([[1,0,1,1,1],[1,0,1,0,1],[1,0,1,1,1],[1,1,1,0,0],[0,0,0,0,1]]))  #-1