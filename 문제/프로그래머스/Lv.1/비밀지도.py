#비밀지도
def solution(n, arr1, arr2):
    answer = []
    a1 = []
    a2 = []
    for i in range(n):
        a1.append(format(arr1[i], 'b').zfill(n))
        a2.append(format(arr2[i], 'b').zfill(n))
    for i, j in zip(a1, a2):
        temp = ""
        for k in range(n):
            if i[k] == j[k] and i[k] == '0':
                temp += ' '
            else:
                temp += '#'
        answer.append(temp)
    return answer

# def solution(n, arr1, arr2):
#     answer = []
#     for i,j in zip(arr1,arr2):
#         a12 = str(bin(i|j)[2:])
#         a12=a12.rjust(n,'0')
#         a12=a12.replace('1','#')
#         a12=a12.replace('0',' ')
#         answer.append(a12)
#     return answer

print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))
