import sys

sys.stdin = open("그래프 경로.txt", "r")


def dfs(adj_l, v, vstd):
    vstd[v] = 1
    for i in adj_l[v]:
        if not vstd[i]:
            dfs(adj_l, i, vstd)


T = int(input())
for tc in range(1, T+1):
    V, E = map(int, input().split())
    adj_l = [[] for _ in range(V+1)]
    vstd = [0]*(V+1)
    for _ in range(E):
        v1, v2 = map(int, input().split())
        adj_l[v1].append(v2)
    S, G = map(int, input().split())
    dfs(adj_l, S, vstd)
    ans = 0
    if vstd[G] == 1:
        ans = 1
    print(f"#{tc} {ans}")
