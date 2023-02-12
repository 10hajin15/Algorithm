#N과 M (3)
from itertools import product
n, m = map(int, input().split())
data = [i for i in range(1, n+1)]
result = list(product(data, repeat=m))
for i in result:
    for j in range(len(i)):
        print(i[j], end=' ')
    print()