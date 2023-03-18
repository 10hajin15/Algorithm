#K번째수
def solution(array, commands):
    answer = []
    for i in commands:
        a, b, c = i
        temp = array[a - 1 : b]
        temp.sort()
        answer.append(temp[c-1])
    return answer

print(solution([1, 5, 2, 6, 3, 7, 4], [[2, 5, 3], [4, 4, 1], [1, 7, 3]]))