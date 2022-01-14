from collections import deque
start, end = map(int, input().split())
count = 0

# def bfs(x, y):
#     q = deque()
#     q.append((x, y))
#     while q:
#         x, y = q.popleft()
#         for i in range(4):
#             nx = x + dx[i]
#             ny = y + dy[i]
#
#             if nx < 0 or nx >= n or ny < 0 or ny >= m:
#                 continue
#             if maze[nx][ny] == 0:
#                 continue
#             if maze[nx][ny] == 1:
#                 maze[nx][ny] = maze[x][y] + 1
#                 q.append((nx, ny))
#     return maze[n - 1][m - 1]
def bfs(start):
    q = deque()
    q.append(start)
    while q:
        now = q.popleft()
        minus = now - 1
        plus = now + 1
        jump = now * 2
        q.append(minus)
        q.append(plus)
        q.append(jump)
        for i in range(3):
            if now > end:








print(count-1)