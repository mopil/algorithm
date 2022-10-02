num_of_catleaf, water, num_of_watering, plus_water = map(int, input().split())

leafs = [water for i in range(num_of_catleaf)]
days = 1
start = 0
i = 0

while True:
    for k in range(num_of_watering):
        leafs[i] += plus_water
        i += 1
    i = i % num_of_catleaf

    for j in range(len(leafs)):
        leafs[j] -= 1

    if 0 in leafs:
        break
    days += 1

print(days)