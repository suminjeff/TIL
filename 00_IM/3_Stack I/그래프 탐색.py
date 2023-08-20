import sys

sys.stdin = open("그래프 탐색.txt", "r")


def dfs(adj_l, v, vstd):
    vstd[v] = 1
    trace.append(v)
    for i in adj_l[v]:
        if vstd[i] == 0:
            dfs(adj_l, i, vstd)


T = 1
for tc in range(1, T+1):
    V, E = map(int, input().split())
    edge = list(map(int, input().split()))
    adj_l = [[] for _ in range(V+1)]
    vstd = [0] * (V+1)
    for i in range(E):
        v1 = edge[2*i]
        v2 = edge[2*i+1]
        adj_l[v1].append(v2)
        adj_l[v2].append(v1)

    trace = []
    dfs(adj_l, 1, vstd)
    print(f"#{tc}", end=" ")
    print(*trace, sep="-")