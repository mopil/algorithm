import heapq
import sys
input = sys.stdin.readline
heap = []


def test(n):
    if n != 0:
        heapq.heappush(heap, n)
        return -1
    else:
        if not heap: return 0
        return heapq.heappop(heap)


n = int(input())
for i in range(n):
    num = test(int(input()))
    if num != -1: print(num)
