row, col = map(int, input().split())
board = [input() for _ in range(row)]
board_list = []


def make_board(axios_x, axios_y):
    if axios_x + 8 > row or axios_y + 8 > col:
        return
    temp_line = []
    flag = False
    for x in range(axios_x, axios_x + 8):
        sliced = board[x][axios_y:axios_y + 8]
        if len(sliced) == 8:
            temp_line.append(sliced)
            flag = True
    if flag:
        board_list.append(temp_line)


for x in range(row):
    for y in range(col):
        make_board(x, y)
print(board_list)
print(len(board_list))