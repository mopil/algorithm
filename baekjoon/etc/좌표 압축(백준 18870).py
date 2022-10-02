import sys

input = sys.stdin.readline
n = int(input())
coord = list(map(int, input().split()))
sorted_coord = sorted(list(set(coord)))
dic = {sorted_coord[i] : i for i in range(len(sorted_coord))}
for i in coord:
    print(dic[i], end=" ")

