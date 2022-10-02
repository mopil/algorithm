# test_case = int(input())
# arr = [0]+[int(input()) for _ in range(test_case)]+[0]
# d = [0] * (test_case + 2)
# d[1], d[2] = arr[1], d[1] + arr[2]
# for i in range(3, test_case+1):
#     d[i] = max(d[i-2], d[i-3]+arr[i-1])+arr[i]
#
# print(d[test_case])

import sys
read = sys.stdin.readline

n = int(read())
stairs = [0] + [int(read()) for _ in range(n)] + [0]
cache = [0] * (n+2)
cache[1] = stairs[1]
cache[2] = cache[1] + stairs[2]

for i in range(3, n+1):
    cache[i] = max(cache[i-2], cache[i-3] + stairs[i-1]) + stairs[i]
print(cache[n])