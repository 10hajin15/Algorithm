#문제 2: 미래도시
INF = int(1e9)

#n은 전체 회사 개수(노드 개수), m은 경로 개수(간선 개수)
n, m = map(int, input().split())

graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에게 가는 비용 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#간선 입력
for _ in range(m):
    #A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1

#x는 최종 목적지, k는 경유지
x, k = map(int, input().split())

#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(1, n+1):
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

distance = graph[1][k] + graph[k][x]

if distance >= INF:
    print("-1")
else:
    print(distance)

#문제해결
#핵심 아이디어: 전형적인 최단 거리 문제이므로 최단 거리 알고리즘을 이용해 해결
#N의 크기가 최대 100이므로 플로이드 워셜 알고리즘을 이용해도 효율적으로 해결할 수 있음
#플로이드 워셜 알고리즘을 수행한 뒤에 (1번 노드에서 X까지의 최단 거리 + X에서 K까지의 최단 거리)를 계산
