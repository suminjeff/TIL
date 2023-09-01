import sys
import time

sys.stdin = open("물놀이를 가자.txt", "r")

start_time = time.time()


def enque(v):
    global rear
    rear += 1
    que[rear] = v


def deque():
    global front
    front += 1
    return que[front]


T = int(input())
for tc in range(1, T+1):
    N, M = map(int, input().split())
    arr = [input() for _ in range(N)]

    que = [0] * (N*M+1)
    front = rear = -1
    visited = [[0]*M for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    ans = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] == "W":
                enque((i, j))
                visited[i][j] = 1

    while front != rear:
        r, c = deque()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < M and visited[nr][nc] == 0:
                enque((nr, nc))
                visited[nr][nc] = visited[r][c] + 1

    for i in range(N):
        for j in range(M):
            if visited[i][j] != 1:
                ans += visited[i][j] - 1

    print(f"#{tc} {ans}")

end_time = time.time()
print("time :", end_time - start_time)