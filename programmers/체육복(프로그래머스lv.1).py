def solution(n, lost, reserve):
    # 여벌이 있는데 도난당했을 수도 있으니 전처리
    set_lost = set(lost) - set(reserve)
    set_reserve = set(reserve) - set(lost)
    for i in set_reserve:
        if i-1 in set_lost:
            set_lost.remove(i-1)
        elif i+1 in set_lost:
            set_lost.remove(i+1)
    return n-len(set_lost)

# n = 5
# lost = [2,4]
# reserve = [1,3,5]
n = 5
lost = [2,4]
reserve = [3]
print(solution(n,lost,reserve))