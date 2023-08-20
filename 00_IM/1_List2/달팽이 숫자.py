import sys

sys.stdin = open("달팽이 숫자.txt", "r")

T = int(input())
for tc in range(1, T + 1):
    N = int(input())
    arr = [[0] * N for _ in range(N)]
    dr = [0, 1, 0, -1]
    dc = [1, 0, -1, 0]
    n = 1
    k = 0
    r = 0
    c = 0
    while n <= N * N:
        arr[r][c] = n
        n += 1
        nr = r + dr[k]
        nc = c + dc[k]
        if 0 <= nr < N and 0 <= nc < N and arr[nr][nc] == 0:
            r = nr
            c = nc
        else:
            k = (k+1) % 4
            r = r + dr[k]
            c = c + dc[k]
    print(f"#{tc}")
    for row in range(N):
        print(*arr[row])