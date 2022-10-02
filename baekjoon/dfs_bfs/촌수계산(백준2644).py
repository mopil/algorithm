from collections import deque


def bfs(start, end):
    queue = deque([start])
    while queue:
        current_node = queue.popleft()
        if current_node == end:
            return True
        for i in lineage[current_node]:
            if visited[i] == 0:
                queue.append(i)
                visited[i] = visited[current_node] + 1
    return False


total_people = int(input())
target = tuple(map(int, input().split()))
pair = int(input())
lineage = [[] for _ in range(total_people+1)]
for _ in range(pair):
    parent, child = map(int, input().split())
    lineage[parent].append(child)
    lineage[child].append(parent)

visited = [0 for _ in range(total_people + 1)]

flag = bfs(target[0], target[1])
result = visited[target[1]]
print(result if flag else -1)
