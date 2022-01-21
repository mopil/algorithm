import time
from collections import deque


class Shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2  # 상어 초기 사이즈는 2
        self.fishes = 0  # 먹은 물고기들


def find_eatable_fish(shark_x, shark_y):
    q = deque()
    q.append((shark_x, shark_y))
    field_copy = [row[:] for row in field]
    eatable_fishes = []

    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            fish_size = field_copy[nx][ny]

            if fish_size < shark.size and field_copy[nx][ny] != 0:
                # 먹을수 있는 물고기면 해당 위치를 더한다
                if (nx, ny) not in eatable_fishes:
                    eatable_fishes.append((nx, ny))

            if (field_copy[nx][ny] == 0 or fish_size == shark.size) and field_copy[nx][ny] != 9:
                field_copy[nx][ny] = 9
                q.append((nx, ny))

    # 더이상 먹을 물고기가 없으면 -1, -1을 리턴
    if not eatable_fishes:
        return -1, -1
    # 그게 아니면 가장 가까운 물고기 좌표를 찾아서 리턴
    else:
        #eatable_fishes.sort()
        result = {}
        for fish_coord in eatable_fishes:
            result[(fish_coord[0], fish_coord[1])] = bfs(shark_x, shark_y, fish_coord[0], fish_coord[1], "find")

        target = min(list(result.values()))
        for item in result.items():  # result 에는 좌표가 키로, 상어가 해당 좌표로 이동하는 이동횟수가 벨류로 들어가 있음
            if item[1] == target:
                return item[0]


def bfs(shark_x, shark_y, fish_x, fish_y, mode):
    q = deque()
    init_x, init_y = shark_x, shark_y
    q.append((shark_x, shark_y))
    field_copy = [row[:] for row in field]
    visited = [([0] * n) for _ in range(n)]

    while q:
        x, y = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            fish_size = field[nx][ny]

            # 상어가 실제로 물고기를 먹는 bfs
            if nx == fish_x and ny == fish_y and mode == "eat":
                # 기존에 상어 위치를 물고기를 먹은 위치로 바꾼다
                field[init_x][init_y] = 0
                field[nx][ny] = 9

                shark.fishes += 1  # 먹은 물고기 추가

                visited[nx][ny] = visited[x][y] + 1

                shark_coord.append((nx, ny))  # 물고기를 먹은 후 해당 위치를 상어 위치로 저장

                return visited[nx][ny]

            # 상어가 주변 물고기를 찾을 때 호출되는 bfs (차이점은 field의 변경 여부)
            if nx == fish_x and ny == fish_y and mode == "find":
                visited[nx][ny] = visited[x][y] + 1
                return visited[nx][ny]

            if (field_copy[nx][ny] == 0 or fish_size == shark.size) and field_copy[nx][ny] != 9:
                field_copy[nx][ny] = 9
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
    return 0


def check_shark_size():
    # 여지껏 먹은 물고기 수가 사이즈랑 동일하면 사이즈 증가
    if shark.fishes == shark.size:
        shark.fishes = 0
        shark.size += 1


def check_end():
    # 끝나는 조건
    # 1. 남아 있는 물고기가 하나도 없을 경우 -> 물고기가 남아 있을 경우 False
    # 2. 남아 있는 물고기가 상어 사이즈보다 모두 크거나 같을 경우 -> 사이즈가 작은 물고기가 존재하면 False
    for i in range(n):
        for j in range(n):
            if field[i][j] <= shark.size:
                return False
    return True


def print_field(field_copy):
    for i in range(n):
        for j in range(n):
            print(field_copy[i][j], end=" ")
        print()


n = int(input())
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))

# 상어 세팅
for i in range(n):
    for j in range(n):
        if field[i][j] == 9:
            shark = Shark(i, j)
            now_shark_x, now_shark_y = i, j
shark_coord = deque()
shark_coord.append((now_shark_x, now_shark_y))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
total_move = 0

# 메인 로직
# 1. 현재 상어 위치에서 현재 크기로 먹을 수 있는 모든 물고기 위치를 탐색한다
# 2. 물고기 위치를 정렬하여 가장 작은값을 돌려준다
# 3. 해당 위치로 가서 물고기를 먹는다
# 4. 끝나는 조건을 만족할 때까지 위를 반복한다
while True:
    now_shark_x, now_shark_y = shark_coord.popleft()

    e_fish_x, e_fish_y = find_eatable_fish(now_shark_x, now_shark_y)

    if e_fish_x == -1 and e_fish_y == -1 or check_end() or shark.size >= 9:
        break

    move = bfs(now_shark_x, now_shark_y, e_fish_x, e_fish_y, "eat")
    print_field(field)
    check_shark_size()
    total_move += move
    print(f"움직인 횟수:{move}, 총 이동수:{total_move}, 상어크기:{shark.size}, 먹은 물고기:{shark.fishes}\n")
print(total_move)







