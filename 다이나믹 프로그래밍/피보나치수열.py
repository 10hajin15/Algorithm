#ex) 피보나치 수열
#1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...
#점화식이란 인접한 항들 사이의 관계식을 의미
#피보나치의 점화식: a(n) = a(n-1) + a(n-2), a1 = 1, a2 = 1 (바로 앞에 있는 수 2개를 더함)

#피보나치 함수(Fibonacci Function)을 재귀함수로 구현

def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

#피보나치 수열의 시간 복잡도 분석
#단순 재귀 함수로 피보나치 수열을 해결하며 지수 시간 복잡도를 가지게 됨 (중복되는 부분 문제)
#-> 위와 같은 코드로 실행해보았을 때, 빅오 표기법을 기준으로 f(30)을 계산하기 위해 약 10억 가량의 연산을 수행해야 함

#메모이제이션(Memoization): Top-down 방식(하향식)
#다이나믹 프로그래밍을 구현하는 방법 중 하나
#한 번 계산한 결과를 메모리 공간에 메모하는 기법
# -> 같은 문제를 다시 호출하면 메모했던 결과를 그대로 가져옴
# -> 값을 기록해 놓는다는 점에서 캐싱(Caching)이라고도 함
#메모이제이션은 이전에 계산된 결과를 일시적으로 기록해 놓는 넓은 개념을 의미
# -> 다이나믹 프로그래밍에 국한된 개념 X
# -> 한 번 계산된 결과를 담아 놓기만 하고 다이나믹 프로그래밍을 위해 활용하지 않을 수도 있음
#메모이제이션을 이용하는 경우 피보나치 수열 함수의 시간 복잡도는 O(N)

#Top-down VS Bottom-up
#탑다운(메모이제이션) 방식은 하향식이라고도 하며 보텀업 방식은 상향식이라고도 함
#다이나믹 프로그래밍의 전형적인 형태는 보텀업 방식
# -> 결과 저장용 리스트는 'DP테이블'이라고 부름

#<피보나치 수열: 탑다운 방식>
#한 번 계산된 결과를 메모이제이션(Memoization)하기 위한 리스트 초기화
d = [0] * 100
#피보나치 함수(Fibonacci Function)를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    #종료 조건(1 혹은 2일 때 1을 반환)
    if x == 1 or x == 2:
        return 1
    #이미 계산한 적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않은 문제라면 점화식에 따라서 피보나치 결과 반환
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]
print(fibo(99))

#<피보나치 수열: 보텀업 방식>
#DP 테이블 초기화
d = [0] * 100
#첫 번쨰 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 99
#피보나치 함수(Fibonacci Function) 반복문으로 구현(보텀업 다이나믹 프로그래밍)
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]
print(d[n])
