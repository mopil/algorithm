n = int(input())
requested_money = list(map(int, input().split()))
budget = int(input())

start, end = 0, max(requested_money)
result = 0
while start <= end:
    mid = (start + end) // 2

    total_money = 0

    for money in requested_money:
        total_money += min(money, mid)

    if budget < total_money:
        end = mid - 1
    else:
        start = mid + 1
print(end)