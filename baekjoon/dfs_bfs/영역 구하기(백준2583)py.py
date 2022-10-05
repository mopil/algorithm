from collections import deque

M, N, K = map(int, input().split())
temp = [list(map(int, input().split())) for _ in range(K)]
graph = [[1] * N for _ in range(M)]

for square in temp:
    x1, y1, x2, y2 = map(int, square)
    for i in range(y1, y2):
        cur_row = (M-1) - i
        for cur_col in range(x1, x2):
            graph[cur_row][cur_col] = 0


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs(x, y):
    q = deque()
    q.append((x, y))
    count = 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= M or ny < 0 or ny >= N:
                continue
            if graph[nx][ny] == 0:
                continue
            if graph[nx][ny] == 1:
                # graph[nx][ny] += graph[x][y]
                graph[nx][ny] = 0
                count += 1
                # for _ in graph:
                #     print(*_)
                # print()
                q.append((nx, ny))
    # return graph[M-1][N-1]
    return count


result = []
chunks = 0
for i in range(M):
    for j in range(N):
        if graph[i][j] == 1:
            cnt = bfs(i, j)
            if cnt == 0: cnt += 1
            result.append(cnt)
            chunks += 1
result.sort()
print(chunks)
print(*result)
