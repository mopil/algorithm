def convert(n, k):
    result = ""
    if k == 10: return str(n)
    current = n
    while current > 0:
        if current % k < 10:
            result += str(current % k)
        current = current // k
    return result[::-1]


def is_prime(n):
    if n == 1: return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0: return False
    return True


def solution(n, k):
    cnt = 0
    converted = convert(n, k)
    for n in converted.split('0'):
        if n == '': continue
        if is_prime(int(n)):
            cnt += 1
    return cnt

solution(437674, 3)
solution(110011, 10)