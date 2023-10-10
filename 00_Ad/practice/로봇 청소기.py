import sys

sys.stdin = open("로봇 청소기.txt", "r")
sys.setrecursionlimit(10**6)


def robot(r, c, d):
    global cnt
    visited[r][c] = 1
    cnt += 1
    nr, nc = r + dr[d], c + dc[d]
    if 0 <= nr < N and 0 <= nc < M and arr[nr][nc] == 0 and visited[nr][nc] == 0:
        robot(nr, nc, d)
    else:
        d = (d+3) % 4
        robot(r, c, d)



N, M = map(int, input().split())
# 0=북, 1=동, 2=남, 3=서
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[0]*M for _ in range(N)]

dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]

cnt = 0
robot(r, c, d)
print(cnt)
