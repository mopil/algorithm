def solution(brown, yellow):
    total = brown + yellow
    for i in range(3, total+1):
        q = total // i  # 세로
        p = total // q  # 가로
        total_brown = (p + q) * 2 - 4
        if total_brown == brown and p >= q and p * q == total:
            return [p, q]