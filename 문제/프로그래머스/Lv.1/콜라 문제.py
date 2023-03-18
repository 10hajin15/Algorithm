#콜라 문제
def solution(a, b, n):
    answer = 0
    while n >= a:
        i = n // a
        j = n % a
        answer += (i * b)
        n = (i * b) + j
    return answer

print(solution(5, 3, 21))