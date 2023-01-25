#문제 2: 문자열 재정렬
from functools import reduce

s = list(input())

result  = list(filter(lambda v: ord(v) >= 65 , s))
num = list(filter(lambda v: ord(v) <= 57 , s))
result.sort()
if num == []: print("".join(result))
else:
    sum = reduce(lambda x, y: int(x) + int(y), num)
    result.append(str(sum))
    print("".join(result))

#문제풀이
#요구사항대로 충실히 구현
#리스트에 저장된 알파벳을 정렬해 출력하고, 합계를 뒤에 붙여 출력하면 정답
# data = input()
# result = []
# value = 0
# #문자를 하나씩 확인하며
# for x in data:
#     #알파벳인 경우 결과 리스트에 삽입
#     if x.isalpha():
#         result.append(x)
#     #숫자는 따로 더하기
#     else:
#         value += int(x)
#
# #알파벳을 오름차순으로 정렬
# result.sort()
#
# #숫자가 하나라도 존재하는 경우 가장 뒤 삽입
# if value != 0:
#     result.append(str(value))
#
# #최종 결과 출력(리스트를 문자열로 변환하여 출력)
# print(''.join(result))