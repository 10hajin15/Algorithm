#가장 가까운 같은 글자
def solution(s):
    answer = []
    for i in range(len(s)):
        temp = s[: i]
        fIndex = temp.rfind(s[i])
        if fIndex == -1:
            answer.append(-1)
        else: answer.append(i - temp.rfind(s[i]))
    return answer

print(solution("banana"))

# def solution(s):
#     answer = []
#     dic = dict()
#     print(dic)
#     for i in range(len(s)):
#         if s[i] not in dic:
#             answer.append(-1)
#         else:
#             answer.append(i - dic[s[i]])
#         dic[s[i]] = i
#     print(dic)
#     return answer

