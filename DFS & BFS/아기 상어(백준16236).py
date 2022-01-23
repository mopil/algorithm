from collections import deque


def bfs():
    global total_move, eat_fishes, shark_size, shark_x, shark_y
    q = deque()
    q.append((shark_x, shark_y))
    visited = [([0] * n) for _ in range(n)]
    fish = []

    # 현재 위치에서 먹을 수 있는 물고기를 탐색한다
    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            if field[nx][ny] > shark_size or visited[nx][ny]:
                continue

            if 0 < field[nx][ny] < shark_size and not visited[nx][ny]:
                visited[nx][ny] = visited[x][y] + 1
                fish.append((visited[nx][ny], nx, ny))  # 물고기의 위치와 그 물고기를 먹으려면 이동해야 하는 횟수를 저장

            # 비어있거나 사이즈도 작고, 한번도 방문 안한 경우
            q.append((nx, ny))
            visited[nx][ny] = visited[x][y] + 1
    #print_field(field)

    # 먹을 물고기가 없으면 False
    if len(fish) <= 0:
        return False
    # 물고리를 먹는다 (물고기 위치랑 상어 위치를 바꾸고 사이즈를 더한다)
    else:
        fish.sort()
        move, fish_x, fish_y = fish[0][0], fish[0][1], fish[0][2]
        total_move += move

        field[shark_x][shark_y] = 0
        field[fish_x][fish_y] = 9
        shark_x, shark_y = fish_x, fish_y

        eat_fishes += 1
        #print(f"움직인 횟수:{move}, 총 이동수:{total_move}, 상어크기:{shark_size}, 먹은 물고기:{eat_fishes}\n")
        if eat_fishes == shark_size:
            eat_fishes = 0
            shark_size += 1

        return True


# def print_field(field_copy):
#     for i in range(n):
#         for j in range(n):
#             print(field_copy[i][j], end=" ")
#         print()


n = int(input())
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))

# 상어 세팅
for i in range(n):
    for j in range(n):
        if field[i][j] == 9:
            shark_x, shark_y = i, j

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_move = 0
shark_size = 2
eat_fishes = 0

while bfs() and shark_size < 9:
    pass
print(total_move)






