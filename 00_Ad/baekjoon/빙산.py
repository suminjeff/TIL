import sys
sys.stdin = open("빙산.txt", "r")
input = sys.stdin.readline
from collections import deque


def dfs(r, c, visited):
    visited[r][c] = 1
    for dr, dc in delta:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] > 0 and not visited[nr][nc]:
            dfs(nr, nc, visited)


def is_connected():
    visited = [[0]*M for _ in range(N)]
    if icebergs:
        dfs(icebergs[0][0], icebergs[0][1], visited)
        for r, c, v, y in icebergs:
            if visited[r][c] == 0:
                return False
        return True
    else:
        return False


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

delta = [[1, 0], [0, 1], [-1, 0], [0, -1]]
sea = [[0]*M for _ in range(N)]

icebergs = deque()
for r in range(N):
    for c in range(M):
        if arr[r][c]:
            icebergs.append((r, c, arr[r][c], 0))
            for dr, dc in delta:
                nr, nc = r + dr, c + dc
                if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0:
                    sea[r][c] += 1

year = 0
while is_connected():
    print(icebergs)
    r, c, v, y = icebergs.popleft()
    v -= sea[r][c]
    if v <= 0:
        v = 0
        for dr, dc in delta:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] >= 0:
                sea[nr][nc] += 1
    else:
        icebergs.append((r, c, v, y+1))
