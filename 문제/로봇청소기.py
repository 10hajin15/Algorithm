#로봇청소기
#방 크기 n * m
# 3 <= n, m <= 50
n, m = map(int, input().split())

#(행, 열) 청소기 위치 (r, c) / 방향
r, c, d = map(int, input().split())

room = []
for _ in range(n):
    room.append(list(map(int, input().split())))

# 북, 동, 남, 서
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

visited = [[0] * m for _ in range(n)]
visited[r][c] = 1
count = 1

while True:
    isAllClean = True
    for i in range(4):
        d = (d + 3) % 4
        nr = r + dr[d]
        nc = c + dc[d]
        if 0 <= nr < n and 0 <= nc < m and room[nr][nc] == 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            count += 1
            r, c = nr, nc
            isAllClean = False
            break
    # 현재 칸의 주변 4칸이 청소되어 있으면
    if isAllClean == True:
        # 후진할 수 없다면
        if room[r - dr[d]][c - dc[d]] == 1:
            break
        else:
            r, c = r - dr[d], c - dc[d]

print(count)













