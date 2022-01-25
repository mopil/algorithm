n = int(input())
result = {}
for _ in range(n):
    temp = input().split('.')[1]
    if temp not in result.keys():
        result[temp] = 1
    else:
        result[temp] += 1
for k, v in sorted(result.items()):
    print(k, v)
