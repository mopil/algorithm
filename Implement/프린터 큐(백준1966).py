cases = int(input())

result = []
for i in range(cases):
    num_of_papers, wonder = map(int, input().split())
    temp = list(map(int, input().split()))
    q = []
    for k in range(num_of_papers):
        q.append([k, temp[k]])

    target = q[wonder]
    printing = 0
    while target in q:
        p = max(temp)
        test = q.pop(0)
        if test[1] < p:
            q.append(test)
        else:
            printing += 1
            temp.remove(p)
    result.append(printing)

print("\n".join(str(i) for i in result))

# 1
# 6 0
# 1 1 9 1 1 1