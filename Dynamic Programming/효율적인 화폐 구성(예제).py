n, m = map(int, input().split())
arr = []
for _ in range(n):
    arr.append(int(input()))

dp = [-1] * 10001
dp[1] = m // max(arr)
for i in range(2, m+1):
    temp = []
    for k in arr:
        temp.append(dp[i] // k)
    dp[i] = min(min(temp), dp[i]) + dp[i-1] + 1
print(dp[m-1])