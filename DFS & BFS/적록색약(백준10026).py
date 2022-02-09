import sys
sys.setrecursionlimit(10000)


def dfs(field, x, y, target):
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if field[x][y] == target:
        field[x][y] = 0
        dfs(field, x, y + 1, target)
        dfs(field, x, y - 1, target)
        dfs(field, x - 1, y, target)
        dfs(field, x + 1, y, target)
        return True
    return False


n = int(input())
normal_field = []
confuse_field = []
for _ in range(n):
    line = input()
    normal_field.append(list(line))

    if "G" in line:
        line = line.replace("G", "R")

    confuse_field.append(list(line))

normal, confuse = 0, 0
for i in range(n):
    for j in range(n):
        for color in ["R", "G", "B"]:
            if dfs(normal_field, i, j, color):
                normal += 1
            if dfs(confuse_field, i, j, color):
                confuse += 1
print(normal, confuse)


