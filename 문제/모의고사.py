#모의고사
a = []
b = []
c = []
for _ in range(2000):
    a.extend([1,2,3,4,5])
for _ in range(1250):
    b.extend([2,1,2,3,2,4,2,5])
for _ in range(1000):
    c.extend([3,3,1,1,2,2,4,4,5,5])

def solution(answers):
    aCount = 0
    bCount = 0
    cCount = 0
    answer = []
    for i in range(len(answers)):
        if a[i] == answers[i]:
            aCount += 1
        if b[i] == answers[i]:
            bCount += 1
        if c[i] == answers[i]:
            cCount += 1
    if max(aCount, bCount, cCount) == aCount:
        answer.append(1)
    if max(aCount, bCount, cCount) == bCount:
        answer.append(2)
    if max(aCount, bCount, cCount) == cCount:
        answer.append(3)
    return answer
print(solution([1,3,2,4,2]))


# def solution(answers):
#     pattern1 = [1,2,3,4,5]
#     pattern2 = [2,1,2,3,2,4,2,5]
#     pattern3 = [3,3,1,1,2,2,4,4,5,5]
#     score = [0, 0, 0]
#     result = []
#
#     for idx, answer in enumerate(answers):
#         if answer == pattern1[idx%len(pattern1)]:
#             score[0] += 1
#         if answer == pattern2[idx%len(pattern2)]:
#             score[1] += 1
#         if answer == pattern3[idx%len(pattern3)]:
#             score[2] += 1
#
#     for idx, s in enumerate(score):
#         if s == max(score):
#             result.append(idx+1)
#
#     return result