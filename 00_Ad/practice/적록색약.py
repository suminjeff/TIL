import sys
sys.stdin = open('적록색약.txt', 'r')
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]


def dfs(r, c, v):
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and arr[r][c] == arr[nr][nc] and visited[nr][nc] == 0:
            visited[nr][nc] = v
            dfs(nr, nc, v)


def cb(r, c, v):
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] != "B" and visited[nr][nc] == 0:
            visited[nr][nc] = v
            cb(nr, nc, v)


N = int(input())
arr = [list(input().rstrip()) for _ in range(N)]

for eye_type in range(2):
    v = 1
    visited = [[0]*N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            if visited[i][j] == 0:
                visited[i][j] = v
                if eye_type == 0:
                    dfs(i, j, v)
                else:
                    if arr[i][j] == "B":
                        dfs(i, j, v)
                    else:
                        cb(i, j, v)
                v += 1
    print(v-1, end=" ")

