arr = list(input())
result = []
for i in range(len(arr)):
    temp = ""
    for j in arr:
        temp += j
    result.append(temp)
    arr.pop(0)

for i in sorted(result):
    print(i)