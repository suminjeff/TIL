import sys
sys.stdin = open('토마토.txt', 'r')
input = sys.stdin.readline
from collections import deque

M, N = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

# 1. bfs를 위한 큐 생성
que = deque()
for i in range(N):
    for j in range(M):
        if arr[i][j] == 1:
            que.append((i, j, 0))

time = 0
# 2. bfs 실행
while que:
    r, c, t = que.popleft()
    if time < t:
        time = t
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
            visited[nr][nc] = 1
            que.append((nr, nc, t+1))

for i in range(N):
    for j in range(M):
        if arr[i][j] == 0 and visited[i][j] == 0:
            print(-1)
            exit()
else:
    print(time)