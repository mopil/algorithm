import itertools

def isPrime(n):
    if n == 2:
        return True
    if n <= 1 or n % 2 == 0:
        return False
    for i in range(2, int(n**0.5)+1):
        if n % i == 0:
            return False
    return True

def solution(s):
    p = []
    for i in range(1, len(s)+1):
        k = list(map("".join, itertools.permutations(s, i)))  # 순열 생성
        p.extend(k)
    p = list(map(int, p))
    p = list(set(p))
    result = []
    for n in p:
        if isPrime(n):
            result.append(n)
    return result
