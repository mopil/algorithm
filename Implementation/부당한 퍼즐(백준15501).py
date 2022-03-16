from collections import deque
import sys
input = sys.stdin.readline
n = int(input())
origin = list(map(int, input().split()))
test = deque(list(map(int, input().split())))


def check(arr1, arr2):
    for i in range(n):
        if arr1[i] != arr2[i]:
            return False
    return True


possible = False
for _ in range(n):
    if check(origin, test):
        possible = True
        break
    test.reverse()
    if check(origin, test):
        possible = True
        break
    test.rotate(-1)
    if check(origin, test):
        possible = True
        break

print("good puzzle" if possible else "bad puzzle")
