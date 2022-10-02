def find_min_flip(n):
    current = n[0]
    count = 0
    for num in n:
        if current != num:
            count += 1
            current = num
    if count % 2 != 0:
        count = (count // 2) + 1
    else:
        count //= 2
    return count


n = list(input())
print(find_min_flip(n))
