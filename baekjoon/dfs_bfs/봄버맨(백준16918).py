def bombed(x, y):
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    if field[x][y] == "O" and not visited[x][y]:
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < row and 0 <= ny < col:
                if field[nx][ny] != "O":
                    field[nx][ny] = "X"
                    visited[nx][ny] = True


def flip():
    for r in range(row):
        for c in range(col):
            if field[r][c] == "X" or field[r][c] == "O":
                field[r][c] = "."
            else:
                field[r][c] = "O"
            visited[r][c] = False


def print_field():
    for i in field:
        print("".join(k for k in i), end="\n")
    print()


row, col, time = map(int, input().split())
field = [list(input()) for _ in range(row)]
full_bombs = ["O"*col for _ in range(row)]
visited = [[False] * col for _ in range(row)]

if time % 2 == 0:
    for i in full_bombs:
        print(i, end="\n")
    exit()

t = time
while True:
    if time <= 1: break
    for r in range(row):
        for c in range(col):
            bombed(r, c)
    time -= 1
    # print(f'{t-time}초 경과 : X는 폭발예정')
    # print_field()
    if time <= 1: break
    flip()
    time -= 1
    # print(f'{t-time}초 경과 : 폭발(플립)')
    # print_field()
print_field()
