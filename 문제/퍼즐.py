#퍼즐
'''
참고: https://velog.io/@dhelee/%EC%9D%BC%EC%9D%BC%EC%BD%94%ED%85%8C-Day14

퍼즐 모양을 1차원 리스트로 생각하기!
문자열(1차원 리스트)에서 0 인덱스 찾기 -> 2차원 배열의 행, 열 인덱스 반환 -> 이동 가능 여부 확인
-> 이동 가능하다면 2차원 배열에서의 위치를 1차원 배열에서의 위치로 변환 -> 해당 위치 값과 0을 swap
-> 방문 여부 체크 -> 큐에 삽입 ㅋ ㅍㅍ=-
'''
from collections import deque

puzzle = ""
for _ in range(3):
    puzzle += "".join(list(input().split()))

visited = {puzzle : 0}      #{퍼즐 리스트 : 이동 횟수}
q = deque([puzzle])

dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

def bfs():
    while q:
        puzzle = q.popleft()
        cnt = visited[puzzle]
        if puzzle == '123456780': return cnt
        z = puzzle.index('0')
        x = z // 3
        y = z % 3
        cnt += 1
        for i in range(4):
            nx = x + dx[i]      #2차원 배열 행
            ny = y + dy[i]      #2차원 배열 열
            if 0 <= nx <= 2 and 0 <= ny <= 2:
                nz = nx * 3 + ny
                puzzle_list = list(puzzle)      #값을 서로 교환하기위해 리스트로 만들어 줌
                puzzle_list[z], puzzle_list[nz] = puzzle_list[nz], puzzle_list[z]   #swap
                new_puzzle = "".join(puzzle_list)

                if visited.get(new_puzzle, 0) == 0:     #방문하지 않았다면
                    visited[new_puzzle] = cnt
                    q.append(new_puzzle)
    return -1

print(bfs())

