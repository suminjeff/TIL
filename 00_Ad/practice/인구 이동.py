import sys
sys.stdin = open("인구 이동.txt", "r")
input = sys.stdin.readline

from collections import deque


def can_move():
    que = deque()
    que.append([0, 0])
    visited = [[0]*N for _ in range(N)]
    while que:
        r, c = que.popleft()
        cnt = 0
        for nr, nc in [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if L <= abs(arr[r][c]-arr[nr][nc]) <= R:
                    cnt += 1
                    return True
                que.append([nr, nc])
    return False

N, L, R = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

while can_move():
    que = deque()
    que.append([0, 0])
    visited = [[0]*N for _ in range(N)]
    total = 0
    while que:
        r, c = que.popleft()
        cnt = 0
        for nr, nc in [[r+1, c], [r, c+1], [r-1, c], [r, c-1]]:
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                if L <= abs(arr[r][c]-arr[nr][nc]) <= R:
                    total += arr[nr][nc]
                que.append([nr, nc])

