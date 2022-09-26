import sys
sys.setrecursionlimit(10000)

def dfs(x, y):
    if x < 0 or x >= h or y < 0 or y >= w:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        dfs(x - 1, y)  # 좌
        dfs(x + 1, y)  # 우
        dfs(x, y + 1)  # 상
        dfs(x, y - 1)  # 하
        dfs(x - 1, y - 1)  # 대각선 하좌
        dfs(x + 1, y - 1)  # 대각선 하우
        dfs(x + 1, y + 1)  # 대각선 상우
        dfs(x - 1, y + 1)  # 대각선 상좌
        return True
    return False


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break

    graph = []
    for i in range(h):
        graph.append(list(map(int, input().split())))
    count = 0

    for i in range(h):
        for j in range(w):
            if dfs(i, j):
                count += 1
    print(count)
