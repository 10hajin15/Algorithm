#문제 1: 전보
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#n 도시개수, m 통로개수, c는 시작 도시
n, m, c = map(int, input().split())

graph = [[] for i in range(n+1)]
distance = [INF] * (n+1)

for _ in range(m):
    x, y, z = map(int, input().split())
    graph[x].append((y, z))     #x에서 y로 가는 시간 z

def dijkstra(c):
    q = []
    heapq.heappush(q, (0, c))
    distance[c] = 0
    while q:
        dist, now = heapq.heappop(q)
        if dist > distance[now]:
            continue
        for i in graph[now]:
            time = dist + i[1]
            if time < distance[i[0]]:
                distance[i[0]] = time
                heapq.heappush(q, (time, i[0]))

dijkstra(c)

count = 0
maxTime = 0
for i in range(1, n+1):
    if c != i and distance[i] != INF:
        count+=1
        if distance[i] > maxTime:
            maxTime = distance[i]

print(count, maxTime)

#문제 풀이
#핵심 아이디어: 한 도시에서 다른 도시까지의 최단 거리 문제로 치환할 수 있음
#N과 M의 범위가 충분히 크기 때문에 우선순위 큐를 활용한 다익스트라 알고리을 구현
# import heapq
# import sys
# input = sys.stdin.readline
# INF = int(1e9)  #무한을 의미하는 값으로 10억을 설정
#
# #노드의 개수, 간선의 개수, 시작 노드를 입력
# n, m, start = map(int, input().split())
# #각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
# graph = [[] for i in range(n+1)]
# #최단 거리 테이블을 모두 무한으로 초기화
# distance = [INF] * (n+1)
#
# #모든 간선 정보 입력받기
# for _ in range(m):
#     x, y, z = map(int, input().split())
#     #x번 노드에서 y번 노드로 가는 비용이 z라는 의미
#     graph[x].append((y, z))
#
# def dijkstra(start):
#     q = []
#     #시작 노드로 가기 위한 최단 거리는 0으로 설정하여, 큐에 삽입
#     heapq.heappush(q, (0, start))
#     distance[start] = 0
#     while q:    #큐가 비어있지 않다면
#         #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
#         dist, now = heapq.heappop(q)
#         if dist > distance[now]:
#             continue
#         #현재 노드와 연결된 다른 인접한 노드들을 확인
#         for i in graph[now]:
#             time = dist + i[1]
#             #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
#             if time < distance[i[0]]:
#                 distance[i[0]] = time
#                 heapq.heappush(q, (time, i[0]))
#
# dijkstra(start)
#
# #도달할 수 있는 노드의 개수
# count = 0
# #도달할 수 있는 노드 중에서, 가장 멀리 있는 노드와의 최단 거리
# max_distance = 0
# for d in distance:
#     #도달할 수 있는 노드인 경우
#     if d != 1e9:
#         count += 1
#         max_distance = max(max_distance, d)
#
# #시작 노드는 제외해야 하므로 count-1 출력
# print(count-1, max_distance)