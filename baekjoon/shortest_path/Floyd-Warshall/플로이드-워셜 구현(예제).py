'''
2차원 배열에 넣어서 생각함 -> 다익스트라 보다 구현이 쉬움
플로이드-워셜은 다이나믹 프로그래밍 유형 중 하나임
시간복잡도는 O(N^3)으로 좀 긴편임
인풋이 500정도만 되서 시간초과가 날 수 있으므로 시간이 충분할 때만 사용
'''

INF = int(1e9)

n = int(input())
m = int(input())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

# 자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if a == b:
            graph[a][b] = 0

# 각 간선에 대한 정보를 입력 받아, 그 값으로 초기화
for _ in range(m):
    # a에서 b로 가는 비용은 c
    a, b, c = map(int, input().split())
    graph[a][b] = c

# 점화식에 따라 플로이드 와샬 알고리즘 수행
for k in range(1, n + 1):
    for a in range(1, n + 1):
        for b in range(1, n + 1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 수행된 결과를 출력
for a in range(1, n + 1):
    for b in range(1, n + 1):
        if graph[a][b] == INF:
            print("INFINITY", end=' ')
        else:
            print(graph[a][b], end=' ')
    print()