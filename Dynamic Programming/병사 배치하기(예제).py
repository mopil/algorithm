'''
가장 긴 증가하는 부분 수열(LIS)알고리즘을 활용
이 문제는 가장 긴 감소하는 부분 수열 알고리즘을 적용해야 해서 뒤집는다
'''

n = int(input())
arr = list(map(int, input().split()))

arr.reverse()

dp = [1] * n

for i in range(1, n):
    for j in range(0, i):
        if arr[j] < arr[i]:
            dp[i] = max(dp[i], dp[j] + 1)

print(n - max(dp))