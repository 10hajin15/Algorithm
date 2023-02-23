# 괄호 회전하기

# 첫번째 시도 -> 실패
# why? [(]) 와 같이 괄호가 겹쳐있을 때도 count가 됨
# def solution(s):
#     left = ['(', '[', '{']
#     right = [')', ']', '}']
#     count = 0
#
#     if len(s) % 2 != 0: return 0
#
#     for i in range(len(s)):
#         sArr = []
#         mArr = []
#         lArr = []
#         tempS = s[i:] + s[:i]
#         for j in tempS:
#             if j in left:
#                 if j == '(': sArr.append(True)
#                 if j == '[': mArr.append(True)
#                 if j == '{': lArr.append(True)
#             if j in right:
#                 if j == ')':
#                     if len(sArr) != 0: sArr.pop()
#                     else:
#                         sArr.append(False)
#                         break
#                 if j == ']':
#                     if len(mArr) != 0: mArr.pop()
#                     else:
#                         mArr.append(False)
#                         break
#                 if j == '}':
#                     if len(lArr) != 0: lArr.pop()
#                     else:
#                         lArr.append(False)
#                         break
#         if len(sArr) + len(mArr) + len(lArr) == 0:
#             count += 1
#     return count

def solution(s):
    left = ['(', '[', '{']
    right = [')', ']', '}']
    count = 0

    if len(s) % 2 != 0: return 0

    for i in range(len(s)):
        newS = s[i:] + s[:i]
        stack = []
        isCount = True
        for j in newS:
            if j in left:
                stack.append(j)
            else:
                if len(stack) == 0:
                    isCount = False
                    break
                else:
                    a = stack.pop()
                    if left.index(a) != right.index(j):
                        isCount = False
                        break
        if isCount: count += 1
    return count