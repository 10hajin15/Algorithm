#문제 2: 1로 만들기
#연산을 사용하는 횟수의 최솟값

#정수 x를 입력 받기
x = int(input())

#앞서 계산된 결과를 저장하기 위한 DP 테이블 초기화
d = [0] * 30001

#다이나믹 프로그래밍(DP) 진행 (보텀업)
for i in range(2, x + 1):
    print("----------------------")
    print("[i]", i)
    d[i] = d[i-1] + 1
    print("1을 뺌")
    if i % 2 == 0:
        print("d[i]은",d[i], "d[i // 2] + 1은",d[i // 2] + 1)
        d[i] = min(d[i], d[i // 2] + 1)
        print("2로 나눔")
    if i % 3 == 0:
        print("d[i]은", d[i], "d[i // 3] + 1은", d[i // 3] + 1)
        d[i] = min(d[i], d[i // 3] + 1)
        print("3로 나눔")
    if i % 5 == 0:
        print("d[i]은", d[i], "d[i // 5] + 1은", d[i // 5] + 1)
        d[i] = min(d[i], d[i // 5] + 1)
        print("5로 나눔")
    print("d[",i,"]", d[i])
    print("----------------------")

print(d[x])