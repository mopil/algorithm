def solution(left, right):
    answer = 0
    for n in range(left, right+1):
        div = []
        for i in range(1, n+1):
            if n % i == 0:
                div.append(i)

        if len(div) % 2 == 0:
            answer += n
        else:
            answer -= n

    return answer