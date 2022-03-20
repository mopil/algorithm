n = int(input())
cost = []
for _ in range(n):
    r, g, b = map(int, input().split())
    cost.append([(r, 0), (g, 1), (b, 2)])

# dp = [0] * (n+1)
# dp.append(min(cost[0]))
# last_index = 0
# result = dp[0][0]
# for i in range(1, n):
#     cost[i].pop(dp[i-1][1])
#     dp.append(min(cost[i]))
#     result += dp[i][0]
# print(result)

dp = [0] * (n+1)
dp[0] = min(cost[0])[0]
last_index = min(cost[0])[1]
for i in range(1, n):
    cost[i].pop(last_index)
    last_index = min(cost[i])[1]
    dp[i] = dp[i-1] + min(cost[i])[0]
print(dp[n-1])