#가장 긴 증가하는 부분 수열
n = int(input())
a = list(map(int, input().split()))
dp = [1] * 1000
for i in range(1, len(a)):
    for j in range(0, i):
        if a[j] < a[i]:
            dp[i] = max(dp[i], dp[j] + 1)
print(max(dp))