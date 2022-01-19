from collections import deque
import sys
scan = sys.stdin.readline


def bfs(node):
    q = deque()
    q.append(node)
    check[node] = 0
    while q:
        node = q.popleft()
        attempt = [node - 1, node + 1]
        # 텔레포트 연결 요소가 존재하면 탐색 후보에 더한다
        if jump[node]:
            attempt += jump[node]

        for n in attempt:
            if (1 <= n <= N) and check[n] == -1:
                q.append(n)
                check[n] = check[node] + 1
            if n == end:
                return check[n]


N, total_connection = map(int, scan().split())
start, end = map(int, scan().split())
jump = [[] for _ in range(N+1)] # 인덱스 에러 진짜 개패고 싶다
check = [-1] * (N + 1)

for _ in range(total_connection):
    a, b = map(int, scan().split())
    jump[a].append(b)
    jump[b].append(a)
cnt = bfs(start)
print(cnt)
