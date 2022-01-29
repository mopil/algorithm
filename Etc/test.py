from collections import deque
def solution(n, times):
    answer = min(times)
    i = 1
    temp = deque()
    while n > 0:
        for t in times:
            temp.append(t * i)
        target = min(temp)
        answer = target
        n -= 1
        temp.popleft(target)
        i += 1
    return answer

solution(6, [7,10])