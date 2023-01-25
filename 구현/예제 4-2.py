# 시각
# 문제 풀이
# 가능한 경우의 수를 모두 검사해보는 탐색 방법인 '완전 탐색(Brute Forcing) 유형'
# 가능한 모든 시각의 경우를 하나씩 모두 세서 풀 수 있는 문제
# 00시 00분 00초부터 23시 59분 59초까지의 모든 경우의 수는 86,400가지(24*60*60)

h = int(input())

count = 0
for i in range(h+1):
    for j in range(60):
        for k in range(60):
            # 매 시각 안에 '3'이 포함되어 있다면 카운트 +1 증가
            if '3' in str(i) + str(j) + str(k):
                count += 1
print(count)