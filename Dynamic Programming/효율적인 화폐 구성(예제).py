# n, m = map(int, input().split())
# arr = []
# for _ in range(n):
#     arr.append(int(input()))
#
# dp = [-1] * 10001
# dp[1] = m // max(arr)
# for i in range(2, m+1):
#     temp = []
#     for k in arr:
#         temp.append(dp[i] // k)
#     dp[i] = min(min(temp), dp[i]) + dp[i-1] + 1
# print(dp[m-1])

n, m = map(int, input().split())

arr = [int(input()) for _ in range(n)]

d = [10001] * (m+1)

d[0] = 0
for i in range(n):
    for j in range(arr[i], m+1):
        if d[j-arr[i]] != 10001:
            d[j] = min(d[j], d[j-arr[i]]+1)
if d[m] == 10001:
    print(-1)
else:
    print(d[m])