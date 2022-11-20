board = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]
q = [[] for _ in range(len(board[0]))]
for y in range(len(board[0])):
    for x in range(len(board)):
        if board[x][y] == 0: continue
        q[y].append(board[x][y])

moves = [1, 2, 3, 4]
result = []
for move in moves:
    try:
        result.append(q[move-1].pop(0))
    except IndexError: continue

stack = []
try:
    stack.append(result[0])
except Exception:
    pass
count, i = 0, 1
while i < len(result):
    if stack[-1] == result[i]:
        try:
            stack.pop()
            count += 2
            i += 1
        except Exception: continue
    else:
        stack.append(result[i])
        i += 1

print(count)