def dfs(x, y):
    if x < 0 or x >= row or y < 0 or y >= col:
        return False

    if field[x][y] == 1:
        field[x][y] = 0

        dfs(x - 1, y)
        dfs(x + 1, y)
        dfs(x, y - 1)
        dfs(x, y + 1)
        return True
    return False


def test():
    for i in range(cab):
        x, y = map(int, input().split())
        field[x][y] = 1

    count = 0
    for i in range(row):
        for j in range(col):
            if dfs(i, j):
                count += 1
    return count


cases = int(input())
for n in range(cases):
    row, col, cab = map(int, input().split())
    field = [[0] * col for i in range(row)]
    print(test(), end='\n')