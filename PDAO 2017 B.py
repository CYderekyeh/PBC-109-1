k = int(input())
a = list(map(int, input().split()))
dp = [0]  * (k+1)
for i in range (1, k+1):
    dp[i] += dp[i-1] - dp[a[i-1]-1] + 2
    dp[i] += dp[i-1]
print(dp[k] % 1000000007)