import sys
import math
sys.setrecursionlimit(10000)
n, m = map(int, input().split())
# print(math.factorial(n)//(math.factorial(n-m)*math.factorial(m)))


# def comb(n, r):
#     return math.factorial(n)//(math.factorial(n-r)*math.factorial(r))

def comb(n, r):
    if n == r:
        return 1
    elif r == 1:
        return n
    if dp[n][r] != 0:
        return dp[n][r]
    dp[n][r] = comb(n-1, r) + comb(n-1, r-1)
    return dp[n][r]


dp = [[0] * (n+1) for _ in range(n+1)]

print(comb(n, m))




