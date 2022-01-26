k, n = map(int, input().split())
arr = [int(input()) for _ in range(k)]
start = 1
end = max(arr)
while start <= end:
    mid = (start + end) // 2
    total = 0
    for lan in arr:
        total += lan // mid

    if total < n:
        end = mid - 1
    else:
        result = mid
        start = mid + 1
print(result)

