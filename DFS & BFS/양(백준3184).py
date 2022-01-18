from collections import deque

def bfs(x, y):
    q = deque()
    q.append((x, y))
    wolf, sheep = 0, 0
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue

            if field[nx][ny] == '#':
                continue
            else:
                if field[nx][ny] == 'v':
                    wolf += 1
                elif field[nx][ny] == 'o':
                    sheep += 1
                field[nx][ny] = '#'
                q.append((nx, ny))
    return wolf, sheep

row, col = map(int, input().split())
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

field = []
for i in range(row):
    field.append(list(input()))

total_wolf, total_sheep = 0, 0
for r in range(row):
    for c in range(col):
        w, s = bfs(r, c)
        if w == s == 0:
            continue
        else:
            if w >= s:
                total_wolf += w
            else:
                total_sheep += s

print(total_sheep, total_wolf)