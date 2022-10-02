from itertools import combinations
import sys
input = sys.stdin.readline


test_case = int(input())
for t in range(test_case):
    items = {}
    for i in range(int(input())):
        not_use, item = map(str, input().split())
        if item not in items.keys(): items[item] = 1
        else: items[item] += 1
    #print(items)

    # 경우의 수 계산
    result = 0
    for way in range(1, len(items.keys())+1):
        for cw in combinations(items.keys(), way):
            total_way = 1
            for c in cw: total_way *= items[c]
            #print(cw, total_way)
            result += total_way
    print(result)


# 1
# 7
# mask face
# sunglasses face
# makeup face
# hi tu
# bye tu
# a alb
# b alb