import sys

sys.stdin = open("정사각형 방.txt", "r")


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
    N = int(input())
    arr = [list(map(int, input().split())) for _ in range(N)]

    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]

    visited = [[0]*N for _ in range(N)]
    que = [0]*(N*N+1)
    front = rear = -1

    for row in range(N):
        for col in range(N):
            enque((row, col))
            visited[row][col] = 1

    while front != rear:
        r, c = deque()
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            if 0 <= nr < N and 0 <= nc < N and visited[nr][nc]:
                visited[nr][nc] = visited[r][c] + 1
                enque((nr, nc))