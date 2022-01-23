from collections import deque
import sys
input = sys.stdin.readline

# def print_field(field_copy):
#     for i in range(n):
#         for j in range(n):
#             print(field_copy[i][j], end=" ")
#         print()


# 현재 위치에서 먹을 수 있는 물고기를 탐색한다
def bfs():
    global shark_size, shark_x, shark_y
    q = deque()
    q.append((shark_x, shark_y, 0))
    visited = [([False] * n) for _ in range(n)]
    visited[shark_x][shark_y] = True
    fish_list = []
    min_dist = int(1e9)

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if field[nx][ny] <= shark_size:
                    visited[nx][ny] = True

                    if 0 < field[nx][ny] < shark_size:
                        min_dist = dist
                        fish_list.append((dist+1, nx, ny))

                    if dist+1 <= min_dist:
                        q.append((nx, ny, dist+1))
    return fish_list

    # print("필드:")
    # print_field(field)
    # print("\n방문:")
    # print_field(visited)
    # 먹을 물고기가 없으면 False


def eat(fish_list):
    global total_move, shark_x, shark_y, eat_fishes, shark_size
    if len(fish_list) <= 0:
        return False
    # 물고리를 먹는다 (물고기 위치랑 상어 위치를 바꾸고 사이즈를 더한다)
    else:
        move, fish_x, fish_y = min(fish_list)
        total_move += move

        field[shark_x][shark_y] = 0
        field[fish_x][fish_y] = 9
        shark_x, shark_y = fish_x, fish_y

        eat_fishes += 1
        # print(f"움직인 횟수:{move}, 총 이동수:{total_move}, 상어크기:{shark_size}, 먹은 물고기:{eat_fishes}\n")
        if eat_fishes == shark_size:
            eat_fishes = 0
            shark_size += 1

        return True


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

while True:
    fish_list = bfs()
    if not eat(fish_list):
        break
print(total_move)





