def compress(arr):
    i = 0
    result = ''
    while i <= len(arr) - 1:
        target = arr[i]
        count = 1
        if i == len(arr) - 1:
            test = arr[i - 1]
            target = arr[i]
        else:
            test = arr[i + 1]
        while target == test and i <= len(arr) - 1:
            test = arr[i]
            if target != test:
                break
            count += 1
            i += 1
        if count == 1:
            result += target
            i += 1
        else:
            result += str(count - 1) + target
    return len(result)


def solution(s):
    if len(s) == 1:
        return 1
    result = compress(list(s))
    for i in range(2, len(s)):
        arr = list([s[j:j + i] for j in range(0, len(s), i)])
        test = compress(arr)
        result = min(test, result)
    return result