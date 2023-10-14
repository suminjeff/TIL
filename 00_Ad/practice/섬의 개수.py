import sys
sys.stdin = open("섬의 개수.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(que):
    while que:
        r, c = que.popleft()
        delta = [[r, c+1], [r+1, c], [r+1, c+1], [r+1, c-1], [r, c-1], [r-1, c], [r-1, c-1], [r-1, c+1]]
        for nr, nc in delta:
            if 0 <= nr < h and 0 <= nc < w and arr[nr][nc] == 1 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append([nr, nc])


while True:
    w, h = map(int, input().split())
    if w == h == 0:
        break
    arr = [list(map(int, input().split())) for _ in range(h)]
    visited = [[0]*w for _ in range(h)]
    cnt = 0
    for i in range(h):
        for j in range(w):
            if arr[i][j] == 1 and visited[i][j] == 0:
                que = deque()
                que.append([i, j])
                visited[i][j] = 1
                bfs(que)
                cnt += 1
    print(cnt)
