from queue import PriorityQueue
import sys
input = sys.stdin.readline

q = PriorityQueue()

for _ in range(int(input())):
    cmd = int(input())
    if cmd == 0:
        if q.empty():
            print(0)
        else:
            print(q.get()[1])
    else:
        q.put((abs(cmd), cmd))
