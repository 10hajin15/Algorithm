#문제 1
n, k = map(int, input().split())

count = 0

while True:
    # n이 k로 나누어 떨어지는 수가 될 때까지 빼기
    target = (n // k) * k
    count = count + (n - target)
    n = target
    # n이 k보다 작을 때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    # k로 나누기
    count += 1
    n //= k

# 마지막으로 남은 수에 대하여 1씩 빼기
count += (n - 1)
print(count)

# 문제 풀이
# 최대한 많이 나누기