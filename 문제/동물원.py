#동물원
# import sys
# input = sys.stdin.readline
# n = int(input())
# d = [[0] * (n+1) for _ in range(n+1)]
# print(d)
# d[0][0] = 1
# d[1][0] = 1
# d[1][1] = 2
# for i in range(2, n+1):
#     for j in range(n+1):
#         if j == 0: d[i][j] = 1
#         else:
#             d[i][j] = (d[i-2][j-1] + d[i-1][j-1] + d[i-1][j]) % 9901
# print(d)
# print(sum(d[n]) % 9901)

n = int(input())
d = [0] * (n+1)
d[0] = 1
d[1] = 3
for i in range(2, n+1):
    d[i] = (d[i-1]*2 + d[i-2]) % 9901
print(d[n])