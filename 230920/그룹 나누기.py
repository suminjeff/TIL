import sys
sys.stdin = open("그룹 나누기.txt", "r")


def dfs(v, isGroup):
    global cnt

    if not visited[v]:
        visited[v] = 1
    if adj_l[v]:
        for w in adj_l[v]:
            if visited[w] == 0:
                dfs(w, 1)
        if isGroup == 0:
            cnt += 1
    else:
        cnt += 1
        return


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = list(map(int, input().split()))
    adj_l = [[] for _ in range(N+1)]
    cnt = 0
    for i in range(M):
        adj_l[arr[2*i]].append(arr[2*i+1])
        adj_l[arr[2*i+1]].append(arr[2*i])
    visited = [0] * (N+1)
    for student in range(1, N+1):
        if not visited[student]:
            dfs(student, 0)

    print(f"#{tc} {cnt}")