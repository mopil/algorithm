def dfs(x, y):
    global count
    if x < 0 or x >= n or y < 0 or y >= n:
        return False

    if graph[x][y] == 1:
        graph[x][y] = 0
        count += 1
        dfs(x, y + 1)
        dfs(x, y - 1)
        dfs(x - 1, y)
        dfs(x + 1, y)
        return True
    return False

n = int(input())
graph = []
count = 0
for i in range(n):
    graph.append(list(map(int, input())))

total_chunks = []
result = 0
for i in range(n):
    for j in range(n):
        if dfs(i, j) == True:
            total_chunks.append(count)
            count = 0
total_chunks.sort()
print(len(total_chunks))
print("\n".join(str(i) for i in total_chunks))