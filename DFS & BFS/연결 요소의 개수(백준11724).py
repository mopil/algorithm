nodes, edges = map(int, input().split())
graph = [[] for _ in range(nodes+1)]
for i in range(edges):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

count = 0
visited = []


def dfs(graph, start):

    global visited
    stack = list()
    stack.append(start)

    while stack:
        node = stack.pop()
        if node not in visited:
            visited.append(node)
            stack.extend(graph[node])


for i in range(1, nodes+1):
    if i not in visited:
        dfs(graph, i)
        count += 1

print(count)