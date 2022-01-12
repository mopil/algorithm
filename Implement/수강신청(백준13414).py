import sys
input = sys.stdin.readline

n, size = map(int, input().split())
d = dict()

for i in range(size):
    key = input().rstrip()
    d[key] = i

d = sorted(d.items(), key = lambda x: x[1])

c = 0
for i in d:
    if c == n:
        break
    print(i[0])
    c += 1
