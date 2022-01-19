from collections import deque
import sys

input = sys.stdin.readline

col, row = map(int, input().split())
graph = []
for i in range(row):
    graph.append(list(map(int, input().split())))

# 전역 큐를 만들어서 익은 토마토 먼저 탐색해서 넣기
q = deque()
for i in range(row):
    # 해당 row 에 1이 있을 때만 탐색 수행
    if 1 in graph[i]:
        for j in range(col):
            if graph[i][j] == 1:
                q.append((i, j))

# 임시 큐
temp = deque()

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]


def bfs():
    global flag
    # bfs 종료 조건 (while:True 빠져나오기)
    if not temp and not q:
        flag = False
        return
    # 임시 큐에 있는 토마토들을 본 큐에 넣는다 (이렇게 하는 이유: 예제3 같은 처음 익은 토마토가 여러개가 존재할 경우를 위해)
    for i in range(len(temp)):
        q.append(temp.popleft())
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if nx < 0 or nx >= row or ny < 0 or ny >= col:
                continue
            if graph[nx][ny] == -1 or graph[nx][ny] == 1:
                continue
            if graph[nx][ny] == 0:
                graph[nx][ny] = 1
                # 본 큐에 넣는게 아닌, 임시 큐에 넣는다
                temp.append((nx, ny))


count = 0
flag = True # 종료 조건 체크

while flag:
    # 상, 하, 좌, 우를 bfs로 탐색해본 후, 익히는 애들만 임시 큐에 넣는다
    # 다음 bfs를 실행하기 전, 임시 큐에 있는 익은 토마토들을 본 큐에 넣고 큐가 빌때까지 수행한다
    bfs()
    count += 1

# 전부 다 익지 못하는 경우 체크
for i in range(row):
    if 0 in graph[i]:
        count = 1

print(count-2)