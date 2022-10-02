lineSize, bucketSize = map(int, input().split())
maxDrops = int(input())
start = 1
end = bucketSize
drops = []
for i in range(0, maxDrops):
    drops.append(int(input()))

move = 0
total = 0
for drop in drops:
    if drop in range(start, end+1):
        continue
    else:
        if drop >= end:
            move = drop - end
            start += move
            end += move
        else:
            move = start - drop
            start -= move
            end -= move
        total += move
print(total)
