import sys
sys.stdin = open("미로 탐색.txt", "r")
input = sys.stdin.readline
from collections import deque


N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
visited = [[0]*M for _ in range(N)]
que = deque()
que.append([0, 0, 1])
visited[0][0] = 1
while que:
    r, c, cnt = que.popleft()
    if r == N-1 and c == M-1:
        print(cnt)
        break
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == '1':
            if visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append([nr, nc, cnt+1])