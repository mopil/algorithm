n, total = map(int, input().split())
coins = sorted([int(input()) for _ in range(n)], reverse=True)
result = 0
for coin in coins:
    coin_num = total // coin
    total -= coin_num * coin
    if total < 0:
        break
    result += coin_num
print(result)
