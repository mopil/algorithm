
n = int(input())

start, end = 0, n
result = 0
while start <= end:
    mid = (start + end) // 2
    if mid ** 2 >= n:
        end = mid - 1
        result = mid
    else:
        start = mid + 1
print(result)

