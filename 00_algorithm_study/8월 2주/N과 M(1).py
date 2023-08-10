import sys

sys.stdin = open("N과 M(1).txt", "r")


def dfs(n, V, adj_m):
    global M
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1
    result = []
    while True:
        for w in range(1, V+1):
            if adj_m[n][w] == 1 and visited[w] == 0:
                stack.append(n)
                n = w
                result.append(n)
                visited[n] = 1
                break
        else:
            if stack:
                n = stack.pop()
            else:
                break
    return result


N, M = map(int, input().split())
arr = [n + 1 for n in range(N)]
adj_m = [[0]*(N+1) for _ in range(N+1)]
for i in range(1, N+1):
    for j in range(1, N+1):
        adj_m[i][j] = 1

print(dfs(1, N, adj_m))
