#계단 오르기
import sys
input = sys.stdin.readline
n = int(input())
d = [0 for _ in range(301)]
score = [0 for _ in range(301)]
for i in range(n):
    score[i] = int(input())
d[0] = score[0]
d[1] = score[0] + score[1]
d[2] = max(score[1]+score[2], score[0]+score[2])
for i in range(3, n):
    d[i] = max(d[i-2], d[i-3]+score[i-1]) + score[i]
print(d[n-1])
