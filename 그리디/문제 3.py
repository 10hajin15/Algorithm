#문제 3: 모험가 길드
n = int(input())
ls = list(map(int, input().split()))
ls.sort()

result = []
temp = []

while len(ls) != 0:
    min = ls[0]
    temp.append(ls[0 : min])
    if temp[0][-1] > len(temp[0]): break
    result.append(temp[0])
    temp = []
    ls = ls[min:]

print(len(result))

# 문제 풀이
# 1) 오름차순 정렬 이후에 공포도가 가장 낮은 모험가부터 하나씩 확인
# 2) 앞에서부터 공포도를 하나씩 확인하며 '현재 그룹에 포함된 모험가의 수'가 '현재 확인하고 있는 공포도'보다
# 크거나 같다면 이를 그룹으로 설정
n = int(input())
data = list(map(int, input().split()))
data.sort()

result = 0  #총 그룹의 수
count = 0   #현재 그룹에 포함된 모험가의 수

for i in data:  #공포도를 낮은 것부터 하나씩 확인하며
    count += 1  #현재 그룹에 해당 모험가를 포함시키기
    if count >= i:  #현재 그룹에 포함된 모험가의 수가 현재의 공포 이상이라면, 그룹 결성
        result += 1 #총 그룹의 수 증가시키기
        count = 0   #현재 그룹에 포함된 모험가의 수 초기화

print(result)   #총 그룹의 수 출력