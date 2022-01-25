n = int(input())
arr = []
for _ in range(n):
    arr.append(input())

확장자 = []
for string in arr:
    dot_index = string.find('.')
    확장자.append(string[dot_index+1:])

result = {}
for i in range(len(확장자)):
    if 확장자[i] not in result.keys():
        result[확장자[i]] = 1
    else:
        result[확장자[i]] += 1

keys = sorted(list(result.keys()))
for i in keys:
    print(i, result[i])