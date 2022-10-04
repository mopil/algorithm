from heapq import heappop, heappush


def dijkstra(n):
    q = []
    heappush(q, (graph[0][0], 0, 0))

    while q:
        now_cost, now_x, now_y = heappop(q)

        if cost[now_x][now_y] < now_cost:
            continue

        for i in range(4):
            next_x = now_x + dx[i]
            next_y = now_y + dy[i]
            if 0 <= next_x < n and 0 <= next_y < n:
                next_cost = graph[next_x][next_y]
                if next_cost + now_cost < cost[next_x][next_y]:
                    heappush(q, (now_cost + next_cost, next_x, next_y))
                    cost[next_x][next_y] = now_cost + next_cost

    return cost[n-1][n-1]


INF = int(1e9)
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
count = 1

while True:
    n = int(input())
    if n == 0: break
    graph = [list(map(int, input().split())) for _ in range(n)]
    cost = [[INF] * n for _ in range(n)]

    result = dijkstra(n)
    print(f'Problem {count}: {result}')
    count += 1



