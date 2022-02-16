import sys
import heapq
input = sys.stdin.readline


for _ in range(int(input())):
    n = int(input())
    q = []
    for _ in range(n):
        cmd, num = input().split()
        num = int(num)
        if cmd == "I":
            heapq.heappush(q, num)

        if not q:
            continue

        if cmd == "D":
            # 최솟값 삭제
            if num == -1:
                heapq.heappop(q)

            # 최댓값 삭제
            elif num == 1:
                q.remove(max(q))

    if not q:
        print("EMPTY")
    else:
        print(max(q), q[0])

# 1
# 9
# I -45
# I 653
# D 1
# I -642
# I 97
# I 97
# D 1
# D -1
# I 97

# 1
# 1
# D -1