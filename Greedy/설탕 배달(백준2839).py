n = int(input())


def find_min_bags(n):
    arr = list()
    for i in range(n+1):
        for j in reversed(range(n+1)):
            sum_bags = i*5 + j*3
            if sum_bags > n:
                continue
            if sum_bags == n:
                arr.append(i+j)
    arr.sort()
    if not arr:
        return -1
    else:
        return arr[0]

print(find_min_bags(n))