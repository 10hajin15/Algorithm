#소수(Prime Number)
#1보다 큰 자연수 중에서 1과 자기 자신을 제외한 자연수로는 나누어 떨어지지 않는 자연수

#소수 판별 함수(2이상 자연수에 대하여)
def is_prime_number(x):
    #2부터 (x-1)까지의 모든 수를 확인하며
    for i in range(2, x):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False    #소수가 아님
    return True     #소수임

#<성능 분석>
#2부터 X-1까지의 모든 자연수에 대하여 연산을 수행
# -> 모든 수를 하나씩 확인한다는 점에서 시간 복잡도는 O(X)

#<약수>
#모든 약수가 가운데 약수를 기준으로 곱셈 연산에 대해 대칭을 이룸
#   -> ex) 16의 약수는 1, 2, 4, 8, 16
#   ->     4를 기준으로 대칭을 이룸
#따라서 특정한 자연수의 모든 약수를 찾을 때 가운데 약수(제곱근)까지만 확인하면 됨

#개선된 소수 판별함수
import math

def is_prime_number(x):
    #2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x)) + 1):
        if x % i == 0:
            return False
    return True

#<성능 분석>
#2부터 X의 제곱근(소수점 이하 무시)까지의 모든 자연수에 대하여 연산을 수행
# -> 시간 복잡도는 O(N 1/2)

