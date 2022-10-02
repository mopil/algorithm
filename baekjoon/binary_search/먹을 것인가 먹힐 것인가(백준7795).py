from bisect import bisect_left

test_case = int(input())
for _ in range(test_case):
    an, bn = map(int, input().split())
    a = sorted(list(map(int, input().split())), reverse=True)
    b = sorted(list(map(int, input().split())))

    total = 0
    for ai in a:
        total += bisect_left(b, ai)
    print(total)
