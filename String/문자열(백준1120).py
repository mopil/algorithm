a, b = map(str, input().split())


def check(str1, str2):
    length = min(len(str1), len(str2))
    count = 0
    for i in range(length):
        if str1[i] != str2[i]:
            count += 1
    return count


def make_permutation(length):
    permutation = []
    for i in range(length+1):
        permutation.append((i, length-i))
    return permutation


if len(a) == len(b):
    print(check(a, b))
else:
    candi = []
    for attempt in make_permutation(len(b) - len(a)):
        start, end = attempt[0], attempt[1]
        if end == 0:
            candi.append(b[start:])
        else:
            candi.append(b[start:-end])
    result = int(1e9)
    for test_str in candi:
        result = min(result, check(a, test_str))
    print(result)