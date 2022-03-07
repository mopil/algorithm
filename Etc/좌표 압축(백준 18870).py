n = int(input())
coord = list(map(int, input().split()))
sorted_coord = sorted(coord)
i = 0
tmp = []
index = 0
while i < len(sorted_coord):
    before = sorted_coord[i - 1]
    now = sorted_coord[i]
    if i >= 1 and before == now:
        pair = tmp[-1]
    else:
        pair = (sorted_coord[i], index)
        index += 1
    i += 1
    tmp.append(pair)

result = []
for n in coord:
    for v, i in tmp:
        if n == v:
            result.append(i)
            break

print(" ".join(str(i) for i in result))
