#숨바꼭질
from collections import deque
n, k = map(int, input().split())
checked = [0] * 100001

def bfs(n):
    queue = deque()
    queue.append(n)
    while queue:
        sb = queue.popleft()
        if sb == k:
            return checked[sb]
        else:
            for i in [sb-1, sb+1, sb*2]:
                if 0 <= i <= 100000 and not checked[i]:
                    checked[i] = checked[sb] + 1
                    queue.append(i)
print(bfs(n))

