def solution(n, computers):
    answer = 0
    visited = [0] * n
    for i in range(n):
        if not visited[i]:
            dfs(n, computers, i, visited)
            answer += 1
    return answer


def dfs(n, computers, i, visited):
    visited[i] = 1
    for j in range(n):
        if i != j and computers[i][j] == 1 and not visited[j]:
            dfs(n, computers, j, visited)


n1 = 3
computers1 = [[1, 1, 0], [1, 1, 0], [0, 0, 1]]

n2 = 3
computers2 = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

ans = solution(n2, computers2)
print(ans)