# 사람을 기준으로 최대한 왼쪽 부터 탐색을 시작한다 (안그러면 마지막 사람은 먹을 수 있는데도 체크를 못 할 수 있다)
N, K = map(int, input().split())
table = list(input())
count = 0
for i in range(len(table)):
    if table[i] == 'P':
        left = max(0, i - K)
        right = min(N, i + K + 1) # range에 넣을거라 마지막을 인덱스로 포함시키려고 +1
        # 왼쪽 부터 탐색할거라, 최초로 햄버거가 등장하면 break하면 됨
        for j in range(left, right):
            if table[j] == 'H':
                table[j] = 0
                count += 1
                break

print(count)

