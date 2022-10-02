import sys
input = sys.stdin.readline
n, m = map(int, input().split())
graph = [[] for _ in range(n+1)]
for _ in range(m):
    start, end = map(int, input().split())
    graph[end].append(start)


def dfs(start):
    visited = []
    stack = list()
    stack.append(start)
    while stack:
        now = stack.pop()
        if now not in visited:
            visited.append(now)
            stack.extend(graph[now])
    return visited


max_count = 0
for node in range(1, n+1):
    if graph[node]:
        result = dfs(node)
        max_count = max(len(result), max_count)
        if len(result) >= max_count:
            print(result[0], end=" ")
