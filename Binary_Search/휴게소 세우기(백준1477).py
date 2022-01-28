현재휴게소개수, 지으려는휴게소개수, 고속도로길이 = map(int, input().split())
rest_coord = sorted(list(map(int, input().split())))

constructable_coord = [i for i in range(고속도로길이) if i not in rest_coord]

# 각 휴게소 끼리 떨어진 간격이 곧 mid가 된다
start, end = 0, 고속도로길이

answer = 0
while start <= end:
    mid = (start + end) // 2

    count = 1  # 휴게소 개수

    current_rest = 0
    for rest in constructable_coord:
        if rest - current_rest >= mid:
            count += 1
            current_rest = rest
            constructable_coord.remove(current_rest)

    if count >= 지으려는휴게소개수:
        start = mid + 1
        answer = mid
    else:
        end = mid - 1
print(answer)




