'''
개미 전사
https://www.youtube.com/watch?v=5Lu34WIx2Us&list=PLRx0vPvlEmdAghTr5mXQxGpHjWqSz0dgC&index=6
27분 쯤
'''

n = int(input())

arr = list(map(int, input().split()))

d = [0] * 100

d[0] = arr[0]
d[1] = max(arr[0], arr[1])

for i in range(2, n):
    d[i] = max(d[i-1], d[i-2] + arr[i])
print(d[n-1])