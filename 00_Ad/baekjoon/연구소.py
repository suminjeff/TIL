import sys
sys.stdin = open("연구소.txt", "r")
input = sys.stdin.readline
from collections import deque
from copy import deepcopy


def comb(s, k, e):
    if s == e:
        possible_arrangement.append(pick[:])
        return

    for i in range(k, len(sample)):
        pick[s] = sample[i]
        comb(s+1, i+1, e)


def virus(picked):
    global max_area
    visited = [[0]*M for _ in range(N)]

    for i in range(3):
        r, c = picked[i]
        arr[r][c] = 1

    while que:
        r, c = que.popleft()
        visited[r][c] = 1
        for dr, dc in [[1, 0], [-1, 0], [0, 1], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
                visited[nr][nc] = 1
                que.append([nr, nc])

    area = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0 and visited[i][j] == 0:
                area += 1
    max_area = max(max_area, area)



N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
initial_area = 0
max_area = 0
que = deque()
sample = []
for i in range(N):
    for j in range(M):
        if arr[i][j] == 0:
            sample.append([i, j])
            initial_area += 1
        elif arr[i][j] == 2:
            que.append([i, j])
pick = [[] for _ in range(3)]
possible_arrangement = []
comb(0, 0, 3)
for pa in possible_arrangement:
    virus(pa)
print(max_area)