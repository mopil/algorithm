pay = int(input())
money = 1000
ex = money - pay
count = 0
coins = [500, 100, 50, 10, 5, 1]
for coin in coins:
    q = ex // coin
    ex -= q * coin
    count += q
print(count)
