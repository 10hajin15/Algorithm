#N과 M (4)
from itertools import combinations_with_replacement

n, m = map(int, input().split())

data = []
for i in range(1, n+1):
    data.append(i)
result = list(combinations_with_replacement(data, m))

for i in result:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()