n = int(input())
arr = [input() for _ in range(n)]
arr2 = list(set(arr))
result = []
max_count = 0
for word in arr2:
    result.append((arr.count(word), word))
    max_count = max(max_count, arr.count(word))
result.sort(key=lambda x: x[1])

for pair in result:
    count, word = pair[0], pair[1]
    if count == max_count:
        print(word)
        break
