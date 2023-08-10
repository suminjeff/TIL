import sys

sys.stdin = open("길찾기.txt", "r")


def dfs(n, V, adj_m):
    stack = []
    visited = [0] * (V+1)
    visited[n] = 1
    result = []
    while True:
        for w in range(1, V):
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


T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    edge = list(map(int, input().split()))
    adj_m = [[0]*100 for _ in range(100)]
    for i in range(E):
        v1, v2 = edge[i*2], edge[i*2+1]
        adj_m[v1][v2] = 1

    ans = 0
    if 99 in dfs(0, 100, adj_m):
        ans = 1
    print(f"#{tc} {ans}")