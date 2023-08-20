import sys

sys.stdin = open("길찾기.txt", "r")

def dfs(adj_l, v, visited):
    visited[v] = 1
    for i in adj_l[v]:
        if not visited[i]:
            dfs(adj_l, i, visited)


T = 10
for _ in range(1, T+1):
    tc, E = map(int, input().split())
    V = 100
    adj_l = [[] for _ in range(V)]
    edge = list(map(int, input().split()))
    for i in range(E):
        adj_l[edge[2*i]].append(edge[2*i+1])
    visited = [0] * (V)
    dfs(adj_l, 0, visited)

    flag = 0
    if visited[99]:
        flag = 1

    print(f"#{tc} {flag}")