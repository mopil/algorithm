def solution(n):
    answer = ''
    while n:
        if n % 3 == 0:
            answer += '4'
            n -= 1
        else:
            answer += str(n%3)
        n //= 3
    return answer[::-1]