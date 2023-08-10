import sys

sys.stdin = open("그래프 탐색.txt", "r")


def dfs(n, V, adj_m):
    # 준비 (스택, 방문여부)
    stack = []
    visited = [0]*(V+1)
    result = []

    # 출발
    visited[n] = 1
    result.append(n)

    while True:
        for w in range(V+1):
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


V, E = map(int, input().split())
T = 1
for tc in range(1, T+1):
    start = 1
    edge = list(map(int, input().split()))
    adj_m = [[0]*(V+1) for _ in range(V+1)]

    for i in range(E):
        v1, v2 = edge[2*i], edge[2*i+1]
        adj_m[v1][v2] = 1
        adj_m[v2][v1] = 1
    ans = dfs(start, V, adj_m)

    print(f"#{tc} ", end="")
    print(*ans, sep="-")
