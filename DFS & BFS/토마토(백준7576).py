from collections import deque
import sys

input = sys.stdin.readline

col, row = map(int, input().split())
graph = []
for i in range(row):
    graph.append(list(map(int, input().split())))

queue = deque()
for i in range(row):
    if 1 in graph[i]:
        for j in range(col):
            if graph[i][j] == 1:
                queue.append((i,j))

temp = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def bfs():
    global flag
    if not temp and not queue:
        flag = False
        return
    for i in range(len(temp)):
        queue.append(temp.popleft())
    while queue:
        x, y = queue.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                temp.append((nx, ny))
count = 0
flag = True
while flag:
    bfs()
    count += 1

for i in range(row):
    if 0 in graph[i]:
        count = 1

print(count-2)