from collections import deque

row, col, k = map(int, input().split())
graph = [[0]*col for _ in range(row)]
for _ in range(k):
    r, c = map(int, input().split())
    graph[r-1][c-1] = 1

dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]


def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue

            if graph[nx][ny] == 0:
                continue

            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                count += 1
                q.append((nx, ny))
    return count


result = 0
for i in range(row):
    for j in range(col):
        if graph[i][j] == 1:
            cnt = bfs(i, j)
            result = max(result, cnt)

print(result)