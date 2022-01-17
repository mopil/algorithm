from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))

    while q:
        x, y = q.popleft()
        for i in range(2):
            move = graph[x][y]
            nx = x + dx[i] * move
            ny = y + dy[i] * move

            if nx >= n or ny >= n:
                continue
            if graph[nx][ny] == -1:
                return True

            q.append((nx, ny))
    return False

def dfs(x, y):
    stack = list()
    stack.append((x, y))
    while stack:
        x, y = stack.pop()
        for i in range(2):
            move = graph[x][y]
            nx = x + dx[i] * move
            ny = y + dy[i] * move

            if nx >= n or ny >= n:
                continue
            if graph[nx][ny] == -1:
                return True

            stack.append((nx, ny))
    return False

n = int(input())
dx = [1, 0]
dy = [0, 1]

graph = []
for i in range(n):
    graph.append(list(map(int, input().split())))

print("HaruHaru" if bfs(0, 0) else "Hing")
