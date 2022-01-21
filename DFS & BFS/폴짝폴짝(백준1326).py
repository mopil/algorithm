from collections import deque


def bfs(x):
    q = deque()
    q.append(x)
    check = [-1] * n
    check[x] = 0
    while q:
        now = q.popleft() # now : 인덱스

        if now == end - 1:
            return check[now]

        for j in range(n):
            if j-now % stones[now] == 0 and check[j] == -1:
                check[j] = check[now] + 1
                q.append(j)
                

n = int(input())
stones = list(map(int, input().split()))
start, end = map(int, input().split())

count = bfs(start-1)

print(count)
#
# 5
# 2 2 2 1 2
# 1 5