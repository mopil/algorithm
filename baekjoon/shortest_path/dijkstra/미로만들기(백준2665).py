from heapq import heappop, heappush
n = int(input())
maze = [list(map(int, input()))for _ in range(n)]
visited = [[False] * n for _ in range(n)]
INF = int(1e9)
cost = [[0] * n for _ in range(n)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

cost[0][0] = 0

q = []
heappush(q, (cost[0][0], 0, 0))

while q:
    now_cost, now_x, now_y = heappop(q)

    for i in range(4):
        next_x = now_x + dx[i]
        next_y = now_y + dy[i]

        if 0 <= next_x < n and 0 <= next_y < n and not visited[next_x][next_y]:
            if maze[next_x][next_y] == 1:
                cost[next_x][next_y] = now_cost
            else:
                cost[next_x][next_y] = now_cost + 1
            heappush(q, (cost[next_x][next_y], next_x, next_y))
            visited[next_x][next_y] = True
print(cost[n-1][n-1])




