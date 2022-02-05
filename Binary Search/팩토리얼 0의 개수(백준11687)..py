'''
https://www.acmicpc.net/problem/11687
팩토리얼 0의 개수 (백준 11687) 골드 5
'''

import math


def find_right_zeros(n):
    digit = str(n)
    zero_count = 0
    for i in range(len(digit), 0, -1):
        if digit[i-1] == '0':
            zero_count += 1
        else:
            break
    return zero_count


fac_list = [math.factorial(i) for i in range(1, 10**2)]

m = int(input())
result = 0
start, end = 0, len(fac_list) - 1
while start <= end:
    mid = (start + end) // 2

    zero_count = find_right_zeros(fac_list[mid])

    if zero_count < m:
        start = mid + 1
    else:
        end = mid - 1
        result = mid

if find_right_zeros(fac_list[result]) != m:
    print(-1)
else:
    print(result+1)
