#숫자 카드
# import sys
# input = sys.stdin.readline
# n = int(input())
# nArr = list(map(int, input().split()))
# m = int(input())
# mArr = list(map(int, input().split()))
# result = []
# for i in mArr:
#     if i in nArr: result.append(1)
#     else: result.append(0)
# for i in result:
#     print(i, end=' ')

import sys
input = sys.stdin.readline
n = int(input())
nArr = set(map(int, input().split()))
m = int(input())
mArr = list(map(int, input().split()))

for i in mArr:
    if i in nArr:
        print(1, end=' ')
    else:
        print(0, end=' ')
