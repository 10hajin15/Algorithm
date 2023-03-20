#푸드 파이트 대회
def solution(food):
    answer = ''
    temp = ''
    for i in range(1, len(food)):
        n = food[i] // 2
        for j in range(n):
            temp += str(i)
    answer += temp
    answer += "0"
    answer += temp[::-1]
    return answer

print(solution([1,3,4,6]))

# def solution(food):
#     answer = ''
#     for i,n in enumerate(food[1:]):
#         answer += str(i+1) * (n//2)
#     return answer + "0" + answer[::-1]