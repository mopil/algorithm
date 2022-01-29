
row, col = map(int, input().split())
field = []
for i in range(row):
    field.append(list(input()))


def row_search(x, y):
    if x >= row or y >= col:
        return False

    if field[x][y] == '-':
        field[x][y] = 0

        row_search(x, y + 1)
        return True
    return False


def col_search(x, y):
    if x >= row or y >= col:
        return False

    if field[x][y] == '|':
        field[x][y] = 0

        col_search(x + 1, y)
        return True
    return False


count = 0

for r in range(row):
    for c in range(col):
        if row_search(r, c):
            count += 1

for r in range(row):
    for c in range(col):
        if col_search(r, c):
            count += 1

print(count)





