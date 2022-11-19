def solution(n, times):
    start, end = 0, n * max(times)
    answer = 0
    while start <= end:
        cur_n = 0
        mid = (start + end) // 2

        for t in times:
            cur_n += mid // t

        if cur_n >= n:
            end = mid - 1
            answer = mid
        else:
            start = mid + 1
    return answer