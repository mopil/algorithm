
total_cases = int(input())
for i in range(total_cases):
    n = int(input())
    logs = list(map(int, input().split()))
    logs.sort()
    result = 0
    for j in range(2, n):
        result = max(result, abs(logs[j] - logs[j-2]))
    print(result)