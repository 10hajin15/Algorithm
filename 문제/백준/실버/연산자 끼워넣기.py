'''
#14888
#연산자 끼워넣기
https://www.acmicpc.net/problem/14888
'''

# from itertools import permutations
#
# n = int(input())
# a = list(map(int, input().split()))
# b = list(map(int, input().split()))
# oper = []
# for i in range(b[0]):
#     oper.append('+')
# for i in range(b[1]):
#     oper.append('-')
# for i in range(b[2]):
#     oper.append('*')
# for i in range(b[3]):
#     oper.append('%')
#
# answer = []
# for j in permutations(oper, n-1):
#     temp = a[0]
#     for k in range(len(j)):
#         if j[k] == '+':
#             temp += a[k+1]
#         elif j[k] == '-':
#             temp -= a[k+1]
#         elif j[k] == '*':
#             temp *= a[k+1]
#         elif j[k] == '%':
#             if temp < 0:
#                 temp = -(abs(temp) // a[k+1])
#             else: temp //= a[k+1]
#     answer.append(temp)
#
# print(max(answer))
# print(min(answer))

import sys

input = sys.stdin.readline
N = int(input())
num = list(map(int, input().split()))
op = list(map(int, input().split()))  # +, -, *, //

maximum = -1e9
minimum = 1e9


def dfs(depth, total, plus, minus, multiply, divide):
    global maximum, minimum
    if depth == N:
        maximum = max(total, maximum)
        minimum = min(total, minimum)
        return

    if plus:
        dfs(depth + 1, total + num[depth], plus - 1, minus, multiply, divide)
    if minus:
        dfs(depth + 1, total - num[depth], plus, minus - 1, multiply, divide)
    if multiply:
        dfs(depth + 1, total * num[depth], plus, minus, multiply - 1, divide)
    if divide:
        dfs(depth + 1, int(total / num[depth]), plus, minus, multiply, divide - 1)


dfs(1, num[0], op[0], op[1], op[2], op[3])
print(maximum)
print(minimum)