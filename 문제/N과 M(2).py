#N과 M (2)
from itertools import combinations
n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
result = list(combinations(data, m))
for i in result:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()