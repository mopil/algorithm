from collections import deque
import time

# class Fish:
#     fish_serial = 0
# 
#     def __init__(self, x, y, size):
#         self.x = x
#         self.y = y
#         self.size = size
#         Fish.fish_serial += 1
#         self.no = Fish.fish_serial
# 
#     def __str__(self):
#         return f"{self.no}번 물고기 좌표:{self.x, self.y}, 사이즈:{self.size}"


class Shark:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.size = 2  # 상어 초기 사이즈는 2
        self.fishes = 0

    def __str__(self):
        return f"좌표:{self.x, self.y}, 사이즈:{self.size}"


def find_eatable_fish(x, y):
    q = deque()
    q.append((x, y))
    field_copy = [row[:] for row in field]
    eatable_fishes = []
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

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

            if (field_copy[nx][ny] == 0 or fish_size == shark.size) and field_copy[nx][ny] != 8:
                field_copy[nx][ny] = 8
                q.append((nx, ny))

    eatable_fishes.sort()
    return eatable_fishes[0]

    # while q:
    #     x, y = q.popleft()
    #     print_field(field_copy)
    #     print_field(visited)
    #     print("--------------------------------")
    #     for i in range(4):
    #         nx = x + dx[i]
    #         ny = y + dy[i]
    #
    #         if nx < 0 or nx >= n or ny < 0 or ny >= n:
    #             continue
    #
    #         fish_size = field_copy[nx][ny]
    #
    #         if fish_size < shark.size and field_copy[nx][ny] != 0:
    #             # 기존에 상어 위치를 물고기를 먹은 위치로 바꾼다
    #             field[init_x][init_y] = 0
    #             field[nx][ny] = 9
    #
    #             shark.fishes.append(1)  # 먹은 물고기 추가
    #
    #             visited[nx][ny] = visited[x][y] + 1
    #
    #             return nx, ny, visited[nx][ny]  # 물고기를 먹어치운 위치를 리턴
    #
    #         if (field_copy[nx][ny] == 0 or fish_size == shark.size) and field_copy[nx][ny] != 8:
    #             field_copy[nx][ny] = 8
    #             visited[nx][ny] = visited[x][y] + 1
    #             q.append((nx, ny))
    #
    # return init_x, init_y, 0  # 먹을 물고기가 없으면 기존 상어 위치를 리턴


def bfs(shark_x, shark_y, fish_x, fish_y):
    q = deque()
    init_x, init_y = shark_x, shark_y
    q.append((shark_x, shark_y))
    field_copy = [row[:] for row in field]
    visited = [([0] * n) for _ in range(n)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]

    while q:
        x, y = q.popleft()
        # print_field(field_copy)
        # print_field(visited)
        # print("--------------------------------")
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if nx < 0 or nx >= n or ny < 0 or ny >= n:
                continue

            fish_size = field[nx][ny]

            if nx == fish_x and ny == fish_y:
                # 기존에 상어 위치를 물고기를 먹은 위치로 바꾼다
                field[init_x][init_y] = 0
                field[nx][ny] = 9

                shark.fishes += 1  # 먹은 물고기 추가

                visited[nx][ny] = visited[x][y] + 1

                return nx, ny, visited[nx][ny]  # 물고기를 먹어치운 위치를 리턴

            if (field_copy[nx][ny] == 0 or fish_size == shark.size) and field_copy[nx][ny] != 8:
                field_copy[nx][ny] = 8
                visited[nx][ny] = visited[x][y] + 1
                q.append((nx, ny))
                
    return init_x, init_y, 0  # 먹을 물고기가 없으면 기존 상어 위치를 리턴


def check_shark_size():
    # 여지껏 먹은 물고기 수가 사이즈랑 동일하면 사이즈 증가
    if shark.fishes == shark.size:
        shark.fishes = 0
        shark.size += 1
        return True
    return False


# def check_end():
#     # 끝나는 조건
#     # 1. 남아 있는 물고기가 하나도 없을 경우
#     # 2. 남아 있는 물고기가 상어 사이즈보다 모두 크거나 같을 경우
#     for i in range(n):
#         for k in range(1, 7):
#             if field[i].count(k) != 0:
#                 return False
#     return True


def print_field(field_copy):
    for i in range(n):
        for j in range(n):
            print(field_copy[i][j], end=" ")
        print()
    print()


n = int(input())
field = []
for _ in range(n):
    field.append(list(map(int, input().split())))

# 자신보다 크면 못지나감. 작으면 먹기 가능. 같으면 먹지는 못하고 지나가기만 가능
for i in range(n):
    for j in range(n):
        if field[i][j] == 9:
            shark = Shark(i, j)
            a, b = i, j

total_move = 0
while True:
    # 메인 로직
    # 1. 현재 상어 위치에서 현재 크기로 먹을 수 있는 모든 물고기 위치를 탐색한다
    # 2. 물고기 위치를 정렬하여 가장 작은값을 돌려준다
    # 3. 해당 위치로 가서 물고기를 먹는다
    # 4. 끝나는 조건을 만족할 때까지 위를 반복한다
    try:
        fish_x, fish_y = find_eatable_fish(a, b)
    except:
        break

    a, b, move = bfs(a, b, fish_x, fish_y)
    print(f"움직인 횟수:{move}, 샤크크기:{shark.size}")

    total_move += move

    # 상어 사이즈 체크
    check_shark_size()

print(total_move)





