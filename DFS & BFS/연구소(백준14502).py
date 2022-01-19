from itertools import combinations
from collections import deque


height, width = map(int, input().split())
graph = []
for i in range(height):
    graph.append(list(map(int, input().split())))

# 벽이 없는 좌표를 가져온다
empty = []
for i in range(height):
    for j in range(width):
        if graph[i][j] == 0:
            empty.append((i, j))
            
# 3개의 벽을 둘 조합을 모두 구한다
wall_case = combinations(empty, 3)


# 3개의 벽의 좌표를 전달받아서 벽을 세운 그래프를 돌려주는 함수
def make_copy(three_walls):
    graph_copy = [item[:] for item in graph]

    for coord in three_walls:
        x, y = coord
        graph_copy[x][y] = 1
    return graph_copy


# 처음 바이러스가 존재하는 위치 찾기
def find_virus_zone():
    virus_zone = []
    for i in range(height):
        for j in range(width):
            if g[i][j] == 2:
                virus_zone.append((i, j))
    return virus_zone


# bfs를 돌면서 바이러스를 퍼트린다
def bfs(x, y):
    q = deque()
    q.append((x, y))
    while q:
        x, y = q.popleft()
        for j in range(4):
            nx = x + dx[j]
            ny = y + dy[j]
            if nx < 0 or nx >= height or ny < 0 or ny >= width:
                continue
            if g[nx][ny] == 2 or g[nx][ny] == 1:
                continue
            if g[nx][ny] == 0:
                g[nx][ny] = 2
                q.append((nx, ny))


# 안전지대 (0인곳) 찾기
def find_safe_zone():
    safe_zone = 0
    for i in range(height):
        safe_zone += g[i].count(0)
    return safe_zone


result = []
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
for case in wall_case:
    g = make_copy(case)
    virus_zone = find_virus_zone()

    for virus_coord in virus_zone:
        a, b = virus_coord
        bfs(a, b)

    result.append(find_safe_zone())

print(max(result))
