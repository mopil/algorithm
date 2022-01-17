from collections import deque
start, end = map(int, input().split())
def bfs():
    dist = [0] * (MAX + 1)
    q = deque()
    q.append(start)
    while q:
        x = q.popleft()
        if x == end:
            print(dist[x])
            break

        for j in (x-1, x+1, x*2):
            if 0 <= j <= MAX and not dist[j]:
                dist[j] = dist[x] + 1
                q.append(j)

MAX = 100000

bfs()