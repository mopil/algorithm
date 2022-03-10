from heapq import heappop, heappush
import sys
input = sys.stdin.readline

v, e = map(int, input().split())
start = int(input())
INF = int(1e9)
graph = [[] for _ in range(v + 1)]
distance = [INF] * (v + 1)

for _ in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))

q = []
heappush(q, (start, 0))
distance[start] = 0

while q:
    now_v, now_cost = heappop(q)
    if distance[now_v] < now_cost:
        continue
    for next_v, next_cost in graph[now_v]:
        cost = now_cost + next_cost
        if cost < distance[next_v]:
            distance[next_v] = cost
            heappush(q, (next_v, cost))

for i in range(1, v + 1):
    print("INF" if distance[i] == INF else distance[i])

