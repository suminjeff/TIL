import sys
sys.stdin = open("연구소.txt", "r")
input = sys.stdin.readline
from collections import deque


def wall(depth):
    if depth == 3:
        virus()
        return
    for i in range(N):
        for j in range(M):
            if arr[i][j] == 0:
                arr[i][j] = 1
                wall(depth+1)
                arr[i][j] = 0


def virus():
    global max_cnt
    z = zero_cnt
    visited = [[False]*M for _ in range(N)]
    que = deque()
    for pr, pc in people:
        que.append([pr, pc])
        visited[pr][pc] = True

    while que:
        r, c = que.popleft()
        for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
            nr, nc = r + dr, c + dc
            if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] is False:
                visited[nr][nc] = True
                z -= 1
                if z <= max_cnt:
                    return
                que.append([nr, nc])
    max_cnt = max(max_cnt, z)


N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
used = [[False]*M for _ in range(N)]
people = []
dq = deque()
zero_cnt = -3
for i in range(N):
    for j in range(M):
        if arr[i][j] == 2:
            people.append([i, j])
            dq.append([i, j])
            used[i][j] = True
        elif arr[i][j] == 0:
            zero_cnt += 1


rows = []
cols = []

while dq:
    r, c = dq.popleft()
    for dr, dc in [[1, 0], [0, 1], [-1, 0], [0, -1]]:
        nr, nc = r + dr, c + dc
        if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and used[nr][nc] is False:
            used[nr][nc] = True
            rows.append(nr)
            cols.append(nc)
            dq.append([nr, nc])
print(rows)
print(cols)


max_cnt = 0
wall(0)
print(max_cnt)