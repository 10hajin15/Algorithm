#두 개 뽑아서 더하기
from itertools import combinations

def solution(numbers):
    answer = []
    for i, j in combinations(numbers, 2):
        answer.append(i + j)
    return sorted(set(answer))

print(solution([2,1,3,4,1]))