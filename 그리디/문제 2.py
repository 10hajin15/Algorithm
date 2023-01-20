#문제 2 : 곱하기 혹은 더하기
s = input()
result = 0

for i in s:
    if (int(i) == 0) or (int(i) == 1) or (result == 0):
        result += int(i)
    else:
        result *= int(i)
print(result)

# 문제 풀이
# 두 수에 대하여 연산을 수행할 때, 두 수 중에서 하나라도 1 이하인 경우에는 더하고,
# 두 수가 모두 2 이상인 경우에는 곱하기
# data = input()
#
# result = int(data[0])
#
# for i in range(1, len(data)):
#     num = int(data[i])
#     if num <= 1 or result <= 1:
#         result += num
#     else:
#         result *= num
# print(result)