#크기가 작은 부분문자열
def solution(t, p):
    answer = 0
    for i in range(len(t) - len(p) + 1):
        temp = t[i : i + len(p)]
        if int(temp) <= int(p):
            answer += 1
    return answer

print(solution("500220839878", "7"))