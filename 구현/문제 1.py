#문제 1: 왕실의 나이트
location = input()
listLoca = list(location)

col = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
row = ['1', '2', '3', '4', '5', '6', '7', '8']

dcol = [-2, -1, 2, 1, -2, -1, 1, 2]
drow = [1, 2, 1, 2, -1, -2, -2, -1]

a = col.index(listLoca[0])
b = row.index(listLoca[1])

count = 0

for i in range(8):
    if a + dcol[i] >= 0 and b + drow[i] >= 0:
        count += 1

print(count)

#문제 풀이
#구현 문제 -> 요구사항대로 충실히 구현

# # 현재 나이트의 위치 입력받기
# input_data = input()
# row = int(input_data[1])
# column = int(ord(input_data[0])) - int(ord('a')) + 1
#
# # 나이트가 이동할 수 있는 8가지 방향 정의
# steps = [(-2, -1), (-1, -2), (1, -2), (2, -1), (2, 1), (1, 2), (-1, 2), (-2, 1)]
#
# # 8가지 방향에 대하여 각 위치로 이동이 가능한지 확인
# result = 0
# for step in steps:
#     # 이동하고자 하는 위치 확인
#     next_row = row + step[0]
#     next_column = column + step[1]
#     # 해당 위치로 이동이 가능하다면 카운트 증가
#     if next_row >= 1 and next_column <= 8 and next_column >= 1 and next_column <= 8:
#         result += 1
#
# print(result)
