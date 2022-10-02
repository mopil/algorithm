from collections import deque
import sys
input = sys.stdin.readline


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


'''
숨바꼭질 처럼 visited에 방문 횟수를 더하면서 진행하면 시간초과가 뜬다 (아마 2차원배열이기 때문에 그런거지 싶다)
그래서 이럴 경우에는 visited를 False로 초기화하고 방문하면 True 한다음에 2차원 배열에 거리 값을 저장하지 않고 따로 다른곳(ex. 큐)에 관리하여야 한다(위 bfs 처럼)
아래 함수는 위 bfs와 똑같은 로직이지만 거리값을 2차원 배열에 넣었는데 시간초과가 발생함을 확인했다
'''
def bfs_2차원더하기방식():
    global shark_size, shark_x, shark_y
    q = deque()
    q.append((shark_x, shark_y, 0))
    visited = [([0] * n) for _ in range(n)]
    fish_list = []
    min_dist = int(1e9)

    while q:
        x, y, dist = q.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0 <= nx < n and 0 <= ny < n and not visited[nx][ny]:
                if field[nx][ny] <= shark_size:
                    visited[nx][ny] = visited[x][y] + 1

                    if 0 < field[nx][ny] < shark_size:
                        min_dist = visited[nx][ny]
                        fish_list.append((visited[nx][ny], nx, ny))

                    if visited[nx][ny] <= min_dist:
                        q.append((nx, ny, visited[nx][ny]))
    return fish_list


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





