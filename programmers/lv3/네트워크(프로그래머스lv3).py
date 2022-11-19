def solution(n, computers):
    answer = 0
    visited = [False] * n
    for com in range(n):
        if not visited[com]:
            dfs(n, computers, com, visited)
            answer += 1 #DFS로 최대한 컴퓨터들을 방문하고 빠져나오게 되면 그것이 하나의 네트워크.
    return answer


def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect != com and computers[com][connect] == 1: #연결된 컴퓨터
            if not visited[connect]:
                dfs(n, computers, connect, visited)