#<에라토스테네스의 체 알고리즘>
#다수의 자연수에 대하여 소수 여부를 판별할 때 사용하는 대표적인 알고리즘
#에라토스테네스의 체는 N보다 작거나 같은 모든 소수를 찾을 때 사용할 수 있음
#동작 과정
#1. 2부터 N까지의 모든 자연수를 나열
#2. 남은 수 중에서 아직 처리하지 않은 가장 작은 수 i를 찾는다.
#3. 남은 수 중에서 i의 배수를 모두 제거한다 (i는 제거하지 않는다.)
#4. 더 이상 반복할 수 없을 때까지 2, 3 과정 반복

import math

n = 1000    #2부터 1,000까지의 모든 수에 대하여 소수 판별
#처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)
array = [True for i in range(n+1)]

#에라토스테네스의 체 알고리즘 수행
#2부터 n의 제곱근까지의 모든 수를 확인하며
for i in range(2, int(math.sqrt(n)) + 1):
    if array[i] == True:    #i가 소수인 경우(남은 수인 경우)
        #i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n:
            array[i*j] = False
            j += 1

#모든 소수 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')

#<성능 분석>
#에라토스테네스의 체 알고리즘의 시간 복잡도는 사실상 선형 시간에 가까울 정도로 매우 빠름
# -> 시간 복잡도는 O(NloglogN)
#에라토스테네스의 체 알고리즘은 다수의 소수를 찾아야 하는 문제에서 효과적으로 사용될 수 있음
# -> 하지만 각 자연수에 대한 소수 여부를 저장해야 하므로 메모리가 많이 필요함