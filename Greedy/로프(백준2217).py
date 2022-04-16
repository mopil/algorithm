n = int(input())
ropes = sorted([int(input()) for _ in range(n)])

length = len(ropes)
result = sum(ropes) // length
for _ in range(n):
    w = sum(ropes) // length
    if ropes[0] < w:
        temp = ropes[0] * length
    else:
        temp = w * length
    ropes.pop(0)
    length -= 1
    result = max(temp, result)
print(result)
