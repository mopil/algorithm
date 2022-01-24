from collections import deque

total_com = int(input())
connect_pair = int(input())

g = [ [] for i in range(total_com+1)] # 0부터 카운트

for i in range(connect_pair):
    a, b = map(int, input().split())
    g[a].append(b)
    g[b].append(a)

count = 0

def dfs_stack(graph, start):
    global count
    stack, visited = list(), list()
    stack.append(start)
    while stack:
        node = stack.pop()

        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])
    return len(visited)-1

def bfs(graph, start):
    q = deque()
    visited = []
    q.append(start)
    while q:
        node = q.popleft()

        for i in graph[node]:
            if i not in visited:
                visited.append(i)
                q.append(i)
    return len(visited)-1

print(bfs(g,1))

