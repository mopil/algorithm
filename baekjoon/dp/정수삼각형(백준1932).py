n = int(input())
dp = [[0] * i for i in range(1, n+1)]
tri = [list(map(int, input().split())) for _ in range(n)]
for level in range(1, len(tri)):
    for index in range(len(tri[level])):
        if index == 0:
            tri[level][index] += tri[level-1][index]
        elif index == level:
            tri[level][index] += tri[level-1][-1]
        else:
            tri[level][index] += max(tri[level-1][index-1], tri[level-1][index])
print(max(tri[-1]))
