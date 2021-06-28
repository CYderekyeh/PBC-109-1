s1, s2 = map(str, input().split())
m = len(s1) 
n = len(s2)
dp = [[0 for x in range(n+1)] for x in range(m+1)]
for i in range(m+1):
    for j in range(n+1):
        if i == 0 or j == 0:
            dp[i][j] = 0
        elif s1[i-1] == s2[j-1]:
            dp[i][j] = dp[i-1][j-1] + 1
        else:
            dp[i][j] = max(dp[i][j-1], dp[i-1][j])
print(m+n-dp[m][n])
