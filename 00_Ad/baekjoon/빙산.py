import sys

sys.stdin = open("빙산.txt", "r")


def adj_list(icebergs):
    adj_l = {}
    for r, c in icebergs:
        value = []
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc]:
                value.append([nr, nc])
        adj_l.setdefault((r, c), value)
    return adj_l


def dfs(p, q, visited, adj_l):
    visited[p][q] = 1
    for r, c in adj_l[(p, q)]:
        if not visited[r][c]:
            dfs(r, c, visited, adj_l)


def isConnected(icebergs):
    global N
    global M
    adj_l = adj_list(icebergs)
    p, q = icebergs[0]
    dfs(p, q, visited, adj_l)
    for r, c in icebergs:
        if visited[r][c] == 0:
            return False
    return True


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dr = [0, 1, 0, -1]
dc = [1, 0, -1, 0]

icebergs = []
for r in range(N):
    for c in range(M):
        if arr[r][c]:
            icebergs.append([r, c])

year = 0
ans = 0
while icebergs:
    temp = [[0]*M for _ in range(N)]
    new_icebergs = []
    for i in range(len(icebergs)):
        r, c = icebergs[i]
        cnt = 0
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and not arr[nr][nc]:
                cnt += 1
        temp[r][c] = 0 if arr[r][c] - cnt <= 0 else arr[r][c] - cnt
        if temp[r][c]:
            new_icebergs.append([r, c])
    for i in range(N):
        for j in range(M):
            arr[i][j] = temp[i][j]
    icebergs = new_icebergs
    year += 1
    if icebergs:
        visited = [[0] * M for _ in range(N)]
        if not isConnected(icebergs):
            ans = year
            break
    else:
        break
print(ans)
