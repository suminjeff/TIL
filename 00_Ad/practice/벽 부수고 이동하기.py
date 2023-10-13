import sys
sys.stdin = open("벽 부수고 이동하기.txt", "r")
input = sys.stdin.readline
from collections import deque


def bfs(que):
    global min_distance
    while que:
        distance, r, c, wall = que.popleft()
        if r == N-1 and c == M-1:
            min_distance = min(min_distance, distance)
            return distance
        delta = [[r + 1, c], [r - 1, c], [r, c + 1], [r, c - 1]]
        for nr, nc in delta:
            if 0 <= nr < N and 0 <= nc < M:
                if arr[nr][nc] == "0":
                    if visited[nr][nc][wall] == 0:
                        visited[nr][nc][wall] = 1
                        que.append((distance+1, nr, nc, wall))
                elif arr[nr][nc] == "1":
                    if wall == 0 and visited[nr][nc][1] == 0:
                        visited[nr][nc][1] = 1
                        que.append((distance+1, nr, nc, 1))


INF = float('inf')
N, M = map(int, input().split())
arr = [input().rstrip() for _ in range(N)]
visited = [[[0, 0] for _ in range(M)] for _ in range(N)]
visited[0][0][0] = 1
que = deque()
que.append((1, 0, 0, 0))
min_distance = INF
bfs(que)
print(min_distance if min_distance != INF else -1)