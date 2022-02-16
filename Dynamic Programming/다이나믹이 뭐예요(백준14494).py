n, m = map(int, input().split())
dp = [[0]*(m+1) for _ in range(n+1)]

for i in range(1, n+1):
    for j in range(1, m+1):
        # # 오른쪽에서 오는 경우
        # if j-1 == 0: from_right = 0
        # else: from_right = dp[i][j-1]
        # # 위쪽에서 오는 경우
        # if i-1 == 0: from_up = 0
        # else: from_up = dp[i-1][j]
        # # 대각선에서 오는 경우
        # if i-1 == 0 and j-1 == 0: from_dia = 0
        # else: from_dia = dp[i-1][j-1]

        if i == 1 and j == 1:
            dp[i][j] = 1
        else: dp[i][j] = dp[i][j-1] + dp[i-1][j] + dp[i-1][j-1]

remain = 10**9 + 7
print(dp[n][m] % remain)